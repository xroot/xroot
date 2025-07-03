# modules/display_manager.py

from modules.settings import BOARD_DIMENSION, DELTA


class DisplayManager:
    def __init__(self, screen):
        self.screen_width, self.screen_height = screen.get_size()
        self.FRACTION_JEU = 1.0  # Si tu veux toute la largeur, sinon 0.7
        self.zone_jeu_width = int(self.screen_width * self.FRACTION_JEU)

        # Dimensions de la zone verte
        ZONE_VERTE_X = 0
        ZONE_VERTE_Y = 0
        ZONE_VERTE_LARGEUR = self.screen_width
        ZONE_VERTE_HAUTEUR = self.screen_height

        # Taille des tuiles pour que tout rentre avec marges DELTA
        self.tile_size = min(
            ZONE_VERTE_LARGEUR / (BOARD_DIMENSION + 2 * DELTA),
            ZONE_VERTE_HAUTEUR / (BOARD_DIMENSION + 2 * DELTA)
        )

        # Offset du plateau
        self.board_offset_x = ZONE_VERTE_X + DELTA * self.tile_size
        self.board_offset_y = ZONE_VERTE_Y + DELTA * self.tile_size

        # Taille réelle du plateau en pixels
        self.total_board_width_pixels = BOARD_DIMENSION * self.tile_size
        self.total_board_height_pixels = BOARD_DIMENSION * self.tile_size

        # --- CHEVALET : position & dimension ---
        self.NUMBER_OF_LETTERS_PER_HAND = 8  # Peut venir d'un .ini

        self.hand_holder_width = self.tile_size * (self.NUMBER_OF_LETTERS_PER_HAND + 0.5)
        self.hand_holder_height = self.tile_size * 1.2

        self.hand_holder_x = (self.screen_width - self.hand_holder_width) / 2
        self.hand_holder_y = self.board_offset_y + self.total_board_height_pixels + 0.5 * self.tile_size

        import pygame
        self.hand_holder_rect = pygame.Rect(
            self.hand_holder_x,
            self.hand_holder_y,
            self.hand_holder_width,
            self.hand_holder_height
        )

        print("-" * 20)
        print("DisplayManager Initialisé :")
        print(f"  Taille écran : {self.screen_width}x{self.screen_height}")
        print(f"  Taille tuile : {self.tile_size}")
        print(f"  Plateau offset X : {self.board_offset_x}")
        print(f"  Plateau offset Y : {self.board_offset_y}")
        print(f"  Plateau W x H : {self.total_board_width_pixels} x {self.total_board_height_pixels}")
        print(f"  Chevalet position : ({self.hand_holder_x}, {self.hand_holder_y})")
        print("-" * 20)
