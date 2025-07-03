# modules/game_logic.py

import pygame
import os

from modules.settings import ASSET_PATH, BOARD_DIMENSION
from modules.player import Player
from modules.letter import Letter
from modules.rules import BOARD_LAYOUT, LETTERS_DOUALA_DISTRIBUTION, Bag
from modules.ui import UIManager
from modules.tile import Tile


class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, size):
        super().__init__()
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)
        except pygame.error:
            print(f"IMAGE INTROUVABLE : {image_path}")
            self.image = pygame.Surface(size)
            self.image.fill((25, 35, 45))
        self.rect = self.image.get_rect(topleft=pos)


class Game:
    def __init__(self, screen, display_manager):
        self.screen = screen
        self.display_manager = display_manager
        self.running = True

        self.background_sprites = pygame.sprite.Group()
        self.grid_sprites = pygame.sprite.Group()
        self.letters_on_board = pygame.sprite.Group()

        self.bag = Bag(LETTERS_DOUALA_DISTRIBUTION)
        player_names = ["Dave", "Jess", "Nay", "Tetang"]
        self.players = [Player(name, 8, self.display_manager) for name in player_names]
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

        self.selected_letter = None
        self.click_offset = (0, 0)

        self.setup_background()
        self.setup_grid()
        self.deal_initial_letters()
        self.ui_manager = UIManager(self.screen, self.display_manager)

        self.print_game_status()

    def setup_background(self):
        width, height = self.display_manager.screen_width, self.display_manager.screen_height
        bg_path = os.path.join(ASSET_PATH, "background", "empty_background.png")
        bg_sprite = BackgroundSprite(bg_path, (0, 0), (width, height))
        self.background_sprites.add(bg_sprite)

    def setup_grid(self):
        TILE_TYPE_MAP = {
            0: "start", 1: "empty", 2: "double_letter", 3: "triple_letter",
            4: "double_word", 5: "triple_word"
        }
        for row in range(BOARD_DIMENSION):
            for col in range(BOARD_DIMENSION):
                tile_type = TILE_TYPE_MAP.get(BOARD_LAYOUT[row][col], "empty")
                tile = Tile(row, col, tile_type, self.display_manager)
                self.grid_sprites.add(tile)

    def deal_initial_letters(self):
        for player in self.players:
            letter_chars = self.bag.draw_letters(8)
            letter_objects = [Letter(char, self.display_manager) for char in letter_chars]
            player.add_letters_to_hand(letter_objects)

    def update(self):
        pass

    def draw(self):
        self.background_sprites.draw(self.screen)
        self.grid_sprites.draw(self.screen)
        self.letters_on_board.draw(self.screen)

        # --- FOND DU CHEVALET ---
        chevalet_path = os.path.join(ASSET_PATH, "background", "hand_holder.png")
        if os.path.exists(chevalet_path):
            img = pygame.image.load(chevalet_path).convert_alpha()
            img = pygame.transform.scale(img, (
                int(self.display_manager.hand_holder_rect.width),
                int(self.display_manager.hand_holder_rect.height)
            ))
            self.screen.blit(img, self.display_manager.hand_holder_rect.topleft)
        else:
            pygame.draw.rect(self.screen, (90, 90, 90), self.display_manager.hand_holder_rect, border_radius=8)

        # --- CHEVALET ACTUEL ---
        self.current_player.draw_hand(self.screen, self.display_manager)

        # --- TEXTE UI ---
        self.ui_manager.draw_game_info(self.current_player, self.bag)

    def print_game_status(self):
        hand_str = ', '.join(sorted([l.character for l in self.current_player.hand.sprites()]))
        print(f"Tour de: {self.current_player.name}, Main: [{hand_str}]")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Clic à la position {event.pos}")
