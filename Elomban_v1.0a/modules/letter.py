# modules/letter.py
import pygame
import os
# On importe seulement ce dont on a besoin
from modules.settings import ASSET_PATH


class Letter(pygame.sprite.Sprite):
    """
    Représente une seule lettre jouable, sous forme de Sprite Pygame.
    """

    def __init__(self, character, display_manager):
        """
        Constructeur de la classe Letter.

        Args:
            character (str): Le caractère de la lettre ('A', 'B', 'E1', etc.).
            display_manager (DisplayManager): L'objet qui gère les dimensions du jeu.
        """
        super().__init__()
        self.character = character

        # Le chemin vers les images des lettres
        image_folder = os.path.join(ASSET_PATH, "letters", "douala")

        image_name = f"{self.character}.png" if self.character != '*' else "joker.png"
        full_path = os.path.join(image_folder, image_name)

        # On récupère la taille de tuile dynamique depuis le manager
        tile_size = display_manager.tile_size

        try:
            self.image = pygame.image.load(full_path).convert_alpha()
        except pygame.error:
            # Plan B si une image manque
            print(f"IMAGE NON TROUVÉE pour la lettre '{character}', création dynamique.")
            self.image = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            self.image.fill((238, 228, 218))
            pygame.draw.rect(self.image, (200, 190, 180), self.image.get_rect(), 2)
            font = pygame.font.SysFont("arial", int(tile_size * 0.7))
            text_surf = font.render(self.character, True, (0, 0, 0))
            text_rect = text_surf.get_rect(center=self.image.get_rect().center)
            self.image.blit(text_surf, text_rect)

        # On dimensionne l'image et on crée le rect
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))

        # On initialise le rect à (0,0). Sa position réelle sera définie
        # par la méthode rearrange_hand() du joueur.
        self.rect = self.image.get_rect(topleft=(0, 0))

    def draw(self, surface):
        """Dessine la lettre sur la surface donnée."""
        surface.blit(self.image, self.rect)
