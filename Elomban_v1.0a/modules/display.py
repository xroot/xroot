import pygame

from modules.settings import BOARD_DIMENSION, DELTA, NUMBER_OF_LETTERS_PER_HAND


class DisplayManager:
    def __init__(self, screen):
        self.NUMBER_OF_LETTERS_PER_HAND = NUMBER_OF_LETTERS_PER_HAND
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
        self.hand_holder_width = self.tile_size * (self.NUMBER_OF_LETTERS_PER_HAND + 0.5)
        self.hand_holder_height = self.tile_size * 1.2

        # Offsets initiaux
        self.hand_holder_offset_x = -300
        self.hand_holder_offset_y = 5

        # Initialisation position chevalet et rect
        self.update_hand_holder_position()

        # print("-" * 20)
        # print("DisplayManager Initialisé :")
        # print(f"  Taille écran : {self.screen_width}x{self.screen_height}")
        # print(f"  Taille tuile : {self.tile_size}")
        # print(f"  Plateau offset X : {self.board_offset_x}")
        # print(f"  Plateau offset Y : {self.board_offset_y}")
        # print(f"  Plateau W x H : {self.total_board_width_pixels} x {self.total_board_height_pixels}")
        # print(f"  Chevalet position : ({self.hand_holder_x}, {self.hand_holder_y})")
        # print("-" * 20)

    def update_hand_holder_position(self):
        """
        Met à jour la position du chevalet et son rectangle en tenant compte des offsets.
        """
        self.hand_holder_x = (self.screen_width - self.hand_holder_width) / 2 + self.hand_holder_offset_x
        self.hand_holder_y = self.screen_height - self.hand_holder_height - self.hand_holder_offset_y

        self.hand_holder_rect = pygame.Rect(
            self.hand_holder_x,
            self.hand_holder_y,
            self.hand_holder_width,
            self.hand_holder_height
        )

    def set_hand_holder_offset(self, offset_x, offset_y):
        """
        Change les offsets du chevalet et met à jour sa position.
        """
        self.hand_holder_offset_x = offset_x
        self.hand_holder_offset_y = offset_y
        self.update_hand_holder_position()

    def get_hand_letter_position(self, index):
        """
        Retourne la position (x, y) en pixels de la lettre d'index donné dans la main pour qu'elle soit centrée sur le chevalet.
        À utiliser partout où une lettre est placée/replacée sur le hand holder.
        Args:
            index (int): index de la lettre dans la main (de 0 à NUMBER_OF_LETTERS_PER_HAND - 1)
        Returns:
            (float, float): position x, y en pixels pour placer la lettre
        """
        # Décalage léger à gauche pour que ce soit bien visuellement (marge)
        offset_x = self.hand_holder_x + 0.1 * self.tile_size
        offset_y = self.hand_holder_y + 0.1 * self.tile_size
        return (
            offset_x + index * self.tile_size,
            offset_y
        )

# Utilisation recommandée dans le code du jeu :
# for i, lettre in enumerate(main_du_joueur):
#     x, y = display_manager.get_hand_letter_position(i)
#     lettre.move_to(x, y)