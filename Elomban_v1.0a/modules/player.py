# modules/player.py
import pygame


class Player:
    """
    Représente un joueur, avec son nom, son score, et sa main de lettres.
    """

    def __init__(self, name, letters_per_hand, display_manager):
        """
        Constructeur de la classe Player.
        """
        self.name = name
        self.score = 0
        self.letters_per_hand = letters_per_hand
        self.display_manager = display_manager
        self.hand = pygame.sprite.Group()

    def add_letters_to_hand(self, letter_objects):
        self.hand.add(letter_objects)
        self.rearrange_hand()

    def remove_letter_from_hand(self, letter_object):
        self.hand.remove(letter_object)
        self.rearrange_hand()

    def rearrange_hand(self):
        """
        Aligne proprement les lettres de la main, en calculant un espacement correct.
        """
        tile_size = self.display_manager.tile_size

        # --- LA MODIFICATION CLÉ POUR LE CHEVALET ---

        # 1. On définit un espacement clair entre les lettres (ex: 10% de la taille d'une tuile)
        spacing = int(tile_size * 1.1)

        # 2. On calcule la largeur totale requise pour la main
        hand_width_pixels = self.letters_per_hand * tile_size + (self.letters_per_hand - 1) * (spacing - tile_size)

        # 3. On calcule la position de départ pour centrer ce bloc
        start_x = (self.display_manager.screen_width - hand_width_pixels) / 2

        # 4. On ajuste la position verticale pour qu'elle soit plus esthétique
        start_y = self.display_manager.screen_height - (2.2 * tile_size)

        for i, letter_sprite in enumerate(self.hand.sprites()):
            # La position de chaque lettre est maintenant calculée avec un espacement fixe.
            letter_sprite.rect.topleft = (start_x + (i * spacing), start_y)

    def draw_hand(self, surface):
        self.hand.draw(surface)

    def __repr__(self):
        hand_str = ', '.join(sorted([l.character for l in self.hand.sprites()]))
        return f"<Player {self.name} | Score: {self.score} | Hand: [{hand_str}]>"
