import pygame
from modules.settings import BOARD_DIMENSION, DELTA


class DisplayManager:
    """
    Calcule et centralise TOUTES les dimensions dynamiques de l'affichage
    en se basant sur les constantes de design de settings.py.
    """

    def __init__(self, screen):
        """
        Initialise le gestionnaire en se basant sur la taille réelle de l'écran.
        La grille est centrée dans la zone verte à gauche, l'UI à droite ne décale plus le plateau.
        """
        self.screen_width, self.screen_height = screen.get_size()

        # --- Fraction de l'écran réservée à la zone de jeu (zone verte, à gauche) ---
        self.FRACTION_JEU = 0.70  # 70% pour le plateau, 30% pour l'UI à droite

        # Largeur effective pour placer le plateau (zone verte uniquement)
        self.zone_jeu_width = int(self.screen_width * self.FRACTION_JEU)

        # --- Calcul de la taille de tuile pour que le plateau tienne dans la zone verte ---
        total_units_vertical = BOARD_DIMENSION + (2 * DELTA)
        total_units_horizontal = BOARD_DIMENSION + (2 * DELTA)

        # Limité par la hauteur ou la largeur "utiles"
        max_tile_size_vert = int(self.screen_height / total_units_vertical)
        max_tile_size_horiz = int(self.zone_jeu_width / total_units_horizontal)
        self.tile_size = min(max_tile_size_vert, max_tile_size_horiz)

        # --- Centrer le plateau dans la zone verte ---
        total_board_width_pixels = total_units_horizontal * self.tile_size
        total_board_height_pixels = total_units_vertical * self.tile_size

        # Offset X : centré dans la zone verte (gauche)
        self.board_offset_x = int((self.zone_jeu_width - total_board_width_pixels) / 2)

        # Offset Y : centré verticalement dans l'écran
        self.board_offset_y = int((self.screen_height - total_board_height_pixels) / 2)

        # --- Affichage pour le débogage ---
        print("-" * 20)
        print("DisplayManager Initialisé :")
        print(f"  Taille réelle de l'écran : {self.screen_width}x{self.screen_height}")
        print(f"  Fraction zone de jeu : {self.FRACTION_JEU}")
        print(f"  Largeur zone de jeu (verte) : {self.zone_jeu_width}")
        print(f"  Taille calculée d'une tuile : {self.tile_size} pixels")
        print(f"  Marge de centrage (Offset X) : {self.board_offset_x} pixels")
        print(f"  Marge supérieure (Offset Y) : {self.board_offset_y} pixels")
        print("-" * 20)
