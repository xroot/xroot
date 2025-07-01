import pygame
import os

# À adapter si la structure diffère
HAND_HOLDER_PATH = os.path.join("assets", "images", "background", "hand_holder.png")

class ChevaletDrawer:
    """
    Dessine le chevalet du joueur, avec fond image.
    """
    def __init__(self, display_manager, screen):
        self.display_manager = display_manager
        self.screen = screen

        # Charge l'image du chevalet
        self.hand_holder_img = pygame.image.load(HAND_HOLDER_PATH).convert_alpha()
        # Redimensionnement de l'image pour coller à la largeur du plateau
        self.hand_holder_img = pygame.transform.smoothscale(
            self.hand_holder_img,
            (int(self.display_manager.total_board_width_pixels), int(self.display_manager.tile_size * self.display_manager.CHEVALET_HEIGHT_TILES))
        )

    def draw(self, player):
        """
        Dessine le fond du chevalet + les lettres du joueur.
        """
        x = self.display_manager.chevalet_offset_x
        y = self.display_manager.chevalet_offset_y

        # Dessine le fond
        self.screen.blit(self.hand_holder_img, (x, y))

        # Dessine les lettres du joueur, centrées sur le chevalet
        hand = player.hand.sprites()
        n = len(hand)
        taille_tuile = self.display_manager.tile_size
        espace = int(taille_tuile * 0.1)

        total_width = n * taille_tuile + (n - 1) * espace
        start_x = x + int((self.hand_holder_img.get_width() - total_width) / 2)
        y_tuile = y + int(self.hand_holder_img.get_height() / 2 - taille_tuile / 2)

        for i, lettre_sprite in enumerate(hand):
            lettre_sprite.rect.topleft = (start_x + i * (taille_tuile + espace), y_tuile)
            self.screen.blit(lettre_sprite.image, lettre_sprite.rect)