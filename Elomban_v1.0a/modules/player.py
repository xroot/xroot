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
        Centre les lettres sur le chevalet via display_manager.get_hand_letter_position.
        """
        for i, letter_sprite in enumerate(self.hand.sprites()):
            x, y = self.display_manager.get_hand_letter_position(i)
            letter_sprite.rect.topleft = (x, y)

    def draw_hand(self, surface, display_manager):
        if not self.hand:
            return

        for i, letter_sprite in enumerate(self.hand.sprites()):
            if letter_sprite:
                x, y = display_manager.get_hand_letter_position(i)
                letter_sprite.rect.topleft = (x, y)
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
