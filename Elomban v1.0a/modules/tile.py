# modules/tile.py
import os

import pygame

from modules.settings import ASSET_PATH  # On a juste besoin du chemin des assets


class Tile(pygame.sprite.Sprite):
    def __init__(self, row, col, tile_type, display_manager):
        super().__init__()

        # Attributs logiques
        self.row = row
        self.col = col
        self.type = tile_type
        self.letter = None

        # --- PARTIE GRAPHIQUE ---
        TILE_IMAGE_PATH = os.path.join(ASSET_PATH, "tiles")
        image_name = f"{tile_type}.png"
        full_path = os.path.join(TILE_IMAGE_PATH, image_name)

        # On récupère la taille et la position depuis le DisplayManager
        tile_size = display_manager.tile_size
        pos_x_pixels = display_manager.board_offset_x + (col * tile_size)
        pos_y_pixels = display_manager.board_offset_y + (row * tile_size)

        try:
            self.image = pygame.image.load(full_path).convert_alpha()
        except pygame.error:
            self.image = pygame.Surface((tile_size, tile_size));
            self.image.fill((100, 100, 100))

        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=(pos_x_pixels, pos_y_pixels))
