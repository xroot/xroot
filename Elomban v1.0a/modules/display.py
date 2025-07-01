# modules/display.py
import pygame
# On importe les "plans" depuis notre source unique de vérité.
from modules.settings import BOARD_DIMENSION, DELTA


class DisplayManager:
    """
    Calcule et centralise TOUTES les dimensions dynamiques de l'affichage
    en se basant sur les constantes de design de settings.py.
    """

    def __init__(self, screen):
        """
        Initialise le gestionnaire en se basant sur la taille réelle de l'écran.
        """
        self.screen_width, self.screen_height = screen.get_size()

        # --- Étape 1: Calculer la taille réelle d'une tuile ---
        # On calcule la dimension totale de notre plateau en "unités de tuile"
        # Pour une grille de 15x15 avec une marge de 1.5 de chaque côté, ça fait 18.
        total_units_vertical = BOARD_DIMENSION + (2 * DELTA)

        # La taille parfaite d'une tuile est donc la hauteur de l'écran divisée par ce nombre.
        self.tile_size = int(self.screen_height / total_units_vertical)

        # --- Étape 2: Calculer les marges de centrage pour un alignement parfait ---

        # On calcule la largeur totale en pixels qu'occupera notre plateau + ses marges.
        total_board_width_pixels = (BOARD_DIMENSION + (2 * DELTA)) * self.tile_size

        # L'offset (la marge à gauche) est l'espace vide restant, divisé par 2.
        self.board_offset_x = int((self.screen_width - total_board_width_pixels) / 2)

        # L'offset vertical est simplement la marge DELTA convertie en pixels.
        self.board_offset_y = int(DELTA * self.tile_size)

        # --- Affichage pour le débogage ---
        print("-" * 20)
        print("DisplayManager Initialisé :")
        print(f"  Taille réelle de l'écran : {self.screen_width}x{self.screen_height}")
        print(f"  Taille calculée d'une tuile : {self.tile_size} pixels")
        print(f"  Marge de centrage (Offset X) : {self.board_offset_x} pixels")
        print(f"  Marge supérieure (Offset Y) : {self.board_offset_y} pixels")
        print("-" * 20)
