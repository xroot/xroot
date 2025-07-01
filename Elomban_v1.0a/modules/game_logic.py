# modules/game_logic.py

import pygame
import os

# --- Imports des modules du projet ---
# On importe uniquement ce dont on a besoin, de manière organisée.
from modules.settings import ASSET_PATH, BOARD_DIMENSION
from modules.player import Player
from modules.letter import Letter
from modules.rules import BOARD_LAYOUT, LETTERS_DOUALA_DISTRIBUTION, Bag
from modules.ui import UIManager
from modules.tile import Tile


# --- Définition de la classe pour les arrières-plans ---
# Cette classe doit hériter de pygame.sprite.Sprite pour être ajoutée à un Groupe.
class BackgroundSprite(pygame.sprite.Sprite):
    """Sprite générique pour charger et afficher les images de fond."""

    def __init__(self, image_path, pos, size):
        super().__init__()  # Indispensable pour un Sprite
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)
        except pygame.error:
            # Plan B si une image est introuvable
            print(f"IMAGE INTROUVABLE : {image_path}")
            self.image = pygame.Surface(size)
            self.image.fill((25, 35, 45))  # Remplit avec un bleu sombre
        self.rect = self.image.get_rect(topleft=pos)


# --- Classe principale de la logique du jeu ---
class Game:
    """
    Orchestre tous les composants du jeu : le plateau, les joueurs,
    la pioche, l'interface et les interactions.
    """

    def __init__(self, screen, display_manager):
        """
        Initialise le jeu avec l'écran et le gestionnaire de dimensions.
        """
        self.screen = screen
        self.display_manager = display_manager
        self.running = True

        # Initialisation des groupes de sprites qui gèrent l'affichage
        self.background_sprites = pygame.sprite.Group()
        self.grid_sprites = pygame.sprite.Group()
        self.letters_on_board = pygame.sprite.Group()

        # Initialisation de la logique du jeu
        self.bag = Bag(LETTERS_DOUALA_DISTRIBUTION)
        player_names = ["Dave", "Jess", "Nay", "Tetang"]
        self.players = [Player(name, 8, self.display_manager) for name in player_names]
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

        # Logique de drag-and-drop
        self.selected_letter = None
        self.click_offset = (0, 0)

        # Mise en place de tous les composants graphiques et logiques
        self.setup_background()
        self.setup_grid()
        self.deal_initial_letters()
        self.ui_manager = UIManager(self.screen, self.display_manager)

        # Affiche le statut initial pour le débogage
        self.print_game_status()

    def setup_background(self):
        """Configure et charge les sprites de l'arrière-plan."""
        width, height = self.display_manager.screen_width, self.display_manager.screen_height
        bg_path = os.path.join(ASSET_PATH, "background", "empty_background.png")
        bg_sprite = BackgroundSprite(bg_path, (0, 0), (width, height))
        self.background_sprites.add(bg_sprite)

    def setup_grid(self):
        """Crée et remplit le groupe de sprites pour la grille de tuiles."""
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
        """Distribue 8 lettres à chaque joueur au début de la partie."""
        for player in self.players:
            letter_chars = self.bag.draw_letters(8)
            letter_objects = [Letter(char, self.display_manager) for char in letter_chars]
            player.add_letters_to_hand(letter_objects)

    def update(self):
        """Met à jour l'état du jeu à chaque frame (sera utile plus tard)."""
        pass

    def draw(self):
        """Dessine tous les éléments du jeu sur l'écran, dans le bon ordre."""
        # 1. Les fonds (le plus en arrière)
        self.background_sprites.draw(self.screen)
        # 2. La grille de tuiles
        self.grid_sprites.draw(self.screen)
        # 3. Les lettres déjà posées sur le plateau
        self.letters_on_board.draw(self.screen)
        # 4. La main du joueur actuel
        self.current_player.draw_hand(self.screen)
        # 5. L'interface utilisateur (textes), par-dessus tout
        self.ui_manager.draw_game_info(self.current_player, self.bag)

    def print_game_status(self):
        """Affiche les informations de départ dans la console."""
        # Note : on utilise .sprites() car la main est un Groupe, pas une liste.
        hand_str = ', '.join(sorted([l.character for l in self.current_player.hand.sprites()]))
        print(f"Tour de: {self.current_player.name}, Main: [{hand_str}]")

    def handle_event(self, event):
        """Gère les entrées de l'utilisateur (sera rempli pour le drag-and-drop).
        :param event:
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Clic à la position {event.pos}")
