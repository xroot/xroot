import pygame
from modules.settings import BOARD_DIMENSION, DELTA

class DisplayManager:
    def __init__(self, screen):
        self.screen_width, self.screen_height = screen.get_size()
        self.FRACTION_JEU = 0.70
        self.zone_jeu_width = int(self.screen_width * self.FRACTION_JEU)
        self.CHEVALET_HEIGHT_TILES = 2

        # dimensions plateau
        total_units_horizontal = BOARD_DIMENSION + (2 * DELTA)

        # dimensions "bloc" vertical (plateau + chevalet)
        total_units_vertical = BOARD_DIMENSION + (2 * DELTA) + self.CHEVALET_HEIGHT_TILES

        # Taille max possible d'une tuile pour que tout tienne dans la zone verte
        max_tile_size_horiz = int(self.zone_jeu_width / total_units_horizontal)
        max_tile_size_vert = int(self.screen_height / total_units_vertical)
        self.tile_size = min(max_tile_size_vert, max_tile_size_horiz)

        # recalcul des dimensions réelles utilisées
        total_board_width_pixels = total_units_horizontal * self.tile_size
        total_board_height_pixels = (BOARD_DIMENSION + 2 * DELTA) * self.tile_size
        chevalet_height_pixels = self.CHEVALET_HEIGHT_TILES * self.tile_size

        bloc_total_height = total_board_height_pixels + chevalet_height_pixels

        # CENTRAGE horizontal dans la zone verte
        self.board_offset_x = int((self.zone_jeu_width - total_board_width_pixels) / 2)
        # CENTRAGE vertical dans la fenêtre pour tout le bloc (plateau+chevalet)
        self.board_offset_y = int((self.screen_height - bloc_total_height) / 2)

        # Chevalet sous le plateau
        self.chevalet_offset_x = self.board_offset_x
        self.chevalet_offset_y = self.board_offset_y + total_board_height_pixels

        self.total_board_width_pixels = total_board_width_pixels
        self.total_board_height_pixels = total_board_height_pixels

        print("-" * 20)
        print("DisplayManager Initialisé :")
        print(f"  Taille écran : {self.screen_width}x{self.screen_height}")
        print(f"  Largeur zone verte : {self.zone_jeu_width}")
        print(f"  Taille tuile : {self.tile_size}")
        print(f"  Plateau offset X : {self.board_offset_x}")
        print(f"  Plateau offset Y : {self.board_offset_y}")
        print(f"  Chevalet offset X : {self.chevalet_offset_x}")
        print(f"  Chevalet offset Y : {self.chevalet_offset_y}")
        print(f"  Hauteur totale bloc (plateau+chevalet): {bloc_total_height}")
        print("-" * 20)