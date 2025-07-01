import pygame
from modules.settings import BOARD_DIMENSION, DELTA

class DisplayManager:
    """
    Calcule et centralise toutes les dimensions dynamiques de l'affichage.
    """

    def __init__(self, screen):
        self.screen_width, self.screen_height = screen.get_size()

        # --- Fraction de l'écran réservée à la zone de jeu (zone verte à gauche) ---
        self.FRACTION_JEU = 0.70  # 70% pour la zone verte (plateau + chevalet)
        self.zone_jeu_width = int(self.screen_width * self.FRACTION_JEU)
        
        # --- Définir la hauteur réservée au chevalet (en tuiles) ---
        # Hauteur réelle de l'image hand_holder.png ou, à défaut, ~2 tuiles
        self.CHEVALET_HEIGHT_TILES = 2
        
        total_units_vertical = BOARD_DIMENSION + (2 * DELTA) + self.CHEVALET_HEIGHT_TILES
        total_units_horizontal = BOARD_DIMENSION + (2 * DELTA)

        # Taille max possible d'une tuile pour que tout tienne dans la zone verte
        max_tile_size_vert = int(self.screen_height / total_units_vertical)
        max_tile_size_horiz = int(self.zone_jeu_width / total_units_horizontal)
        self.tile_size = min(max_tile_size_vert, max_tile_size_horiz)

        # Dimensions du plateau (hors chevalet)
        total_board_width_pixels = total_units_horizontal * self.tile_size
        total_board_height_pixels = (BOARD_DIMENSION + 2 * DELTA) * self.tile_size

        # --- Centrer le plateau dans la zone verte ---
        self.board_offset_x = int((self.zone_jeu_width - total_board_width_pixels) / 2)
        # Décalage vertical : centré dans la zone verte en tenant compte du chevalet
        zone_verte_height = self.screen_height
        self.board_offset_y = int((zone_verte_height - (total_board_height_pixels + self.CHEVALET_HEIGHT_TILES * self.tile_size)) / 2)

        # --- Position du chevalet ---
        # Centré horizontalement sous le plateau, juste en dessous
        self.chevalet_offset_x = self.board_offset_x
        self.chevalet_offset_y = self.board_offset_y + total_board_height_pixels

        # --- Pour accès par d'autres modules ---
        self.total_board_width_pixels = total_board_width_pixels
        self.total_board_height_pixels = total_board_height_pixels

        # Debug
        print("-" * 20)
        print("DisplayManager Initialisé :")
        print(f"  Taille écran : {self.screen_width}x{self.screen_height}")
        print(f"  Largeur zone verte : {self.zone_jeu_width}")
        print(f"  Taille tuile : {self.tile_size}")
        print(f"  Plateau offset X : {self.board_offset_x}")
        print(f"  Plateau offset Y : {self.board_offset_y}")
        print(f"  Chevalet offset X : {self.chevalet_offset_x}")
        print(f"  Chevalet offset Y : {self.chevalet_offset_y}")
        print("-" * 20)