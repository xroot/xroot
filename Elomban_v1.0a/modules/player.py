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

    def draw_hand(self, surface, display_manager):
        """
        Dessine la main du joueur sur la surface donnée, en suivant la position du chevalet.
        """
        if not self.hand:
            return

        # Décalage du chevalet vers la droite et vers le haut
        display_manager.set_hand_holder_offset(1, 20)

        # Point de départ horizontal pour le dessin des pièces (légèrement décalé pour centrer dans le chevalet)
        x_start = display_manager.hand_holder_x + 0.25 * display_manager.tile_size

        # Décalage vertical pour aligner les pièces avec le fond du chevalet
        y = display_manager.hand_holder_y + 0.25 * display_manager.tile_size

        # Espacement entre les pièces (tuile + marge)
        spacing = int(display_manager.tile_size * 1.1)

        for i, letter_sprite in enumerate(self.hand.sprites()):
            if letter_sprite:
                letter_sprite.rect.topleft = (
                    x_start + i * spacing,
                    y
                )
                surface.blit(letter_sprite.image, letter_sprite.rect)

    def __repr__(self):
        """ Représentation textuelle de l'objet Player. """
        if not self.hand:
            return f"<Player {self.name} | Score: {self.score} | Hand: []>"

        # On trie les lettres de la main pour une représentation cohérente
        if not self.hand.sprites():
            return f"<Player {self.name} | Score: {self.score} | Hand: []>"

        # On crée une chaîne de caractères avec les lettres triées
        hand_str = ', '.join(sorted([l.character for l in self.hand.sprites()]))
        return f"<Player {self.name} | Score: {self.score} | Hand: [{hand_str}]>"

    def reset_score(self):
        """
        Réinitialise le score du joueur à zéro.
        """
        self.score = 0

    def add_score(self, points):
        """
        Ajoute des points au score du joueur.
        """
        self.score += points
        print(f"{self.name} a maintenant {self.score} points.")

    def clear_hand(self):
        """
        Vide la main du joueur.
        """
        self.hand.empty()
        print(f"La main de {self.name} a été vidée.")

    def get_hand_size(self):
        """
        Retourne la taille de la main du joueur.
        """
        return len(self.hand)

    def get_hand_letters(self):
        """
        Retourne une liste des lettres dans la main du joueur.
        """
        return [letter.character for letter in self.hand.sprites()]

    def has_letters(self):
        """
        Vérifie si le joueur a des lettres dans sa main.
        """
        return len(self.hand) > 0

    def has_letter(self, letter):
        """
        Vérifie si le joueur a une lettre spécifique dans sa main.
        """
        return any(l.character == letter for l in self.hand.sprites())

    def __eq__(self, other):
        """
        Compare deux joueurs par leur nom.
        """
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        """
        Retourne le hash du joueur basé sur son nom.
        """
        return hash(self.name)

    def __lt__(self, other):
        """
        Compare deux joueurs par leur score pour le tri.
        """
        if not isinstance(other, Player):
            return NotImplemented
        return self.score < other.score

    def __gt__(self, other):
        """
        Compare deux joueurs par leur score pour le tri.
        """
        if not isinstance(other, Player):
            return NotImplemented
        return self.score > other.score

    def __le__(self, other):
        """
        Compare deux joueurs par leur score pour le tri.
        """
        if not isinstance(other, Player):
            return NotImplemented
        return self.score <= other.score

    def __ge__(self, other):
        """
        Compare deux joueurs par leur score pour le tri.
        """
        if not isinstance(other, Player):
            return NotImplemented
        return self.score >= other.score

    def __ne__(self, other):
        """
        Compare deux joueurs par leur nom pour l'inégalité.
        """
        if not isinstance(other, Player):
            return NotImplemented
        return self.name != other.name

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le joueur.
        """
        return f"Player(name={self.name}, score={self.score}, hand_size={len(self.hand)})"

    def __len__(self):
        """
        Retourne la taille de la main du joueur.
        """
        return len(self.hand)

    def __contains__(self, letter):
        """
        Vérifie si une lettre est dans la main du joueur.
        """
        return any(l.character == letter for l in self.hand.sprites())

    def __iter__(self):
        """
        Permet d'itérer sur les lettres de la main du joueur.
        """
        return iter(self.hand.sprites())

    def __getitem__(self, index):
        """
        Permet d'accéder à une lettre spécifique dans la main du joueur.
        """
        if index < 0 or index >= len(self.hand):
            raise IndexError("Index hors limites pour la main du joueur.")
        return self.hand.sprites()[index]
