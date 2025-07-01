# modules/rules.py
import random

LETTERS_DOUALA_DISTRIBUTION = {
    'E': 12, 'A': 9, 'I': 8, 'O': 7, 'U': 6, 'N': 6, 'L': 5, 'S': 5,
    'E1': 5,  # Représente Ɛ
    'M': 4, 'T': 4, 'B': 4,
    'K': 3, 'D': 3,
    'N1': 3,  # Représente ñ
    'O1': 3,  # Représente Ɔ
    'R': 2, 'F': 2, 'G': 2, 'H': 2, 'Z': 2,
    'V': 1, 'J': 1,
    'N2': 1,  # Représente  Ṅ
    'Y': 1, 'W': 1, 'X': 1,
    '*': 2  # 2 Jokers selon le standard FR
}

POINTS_DOUALA = {
    '*': 0, 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'E1': 2, 'F': 4, 'G': 3, 'H': 4,
    'I': 1, 'J': 8, 'K': 4, 'L': 1, 'M': 2, 'N': 1, 'N1': 4, 'N2': 10, 'O1': 5, 'O': 1,
    'P': 3, 'R': 2, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 10, 'Y': 4, 'Z': 5
}

BOARD_LAYOUT = [
    [5, 1, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 1, 5], [1, 1, 3, 1, 1, 4, 1, 1, 1, 4, 1, 1, 3, 1, 1],
    [1, 3, 1, 1, 4, 1, 1, 2, 1, 1, 4, 1, 1, 3, 1], [3, 1, 1, 4, 1, 1, 3, 1, 3, 1, 1, 4, 1, 1, 3],
    [1, 1, 4, 1, 1, 2, 1, 2, 1, 2, 1, 1, 4, 1, 1], [1, 4, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 4, 1],
    [3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3], [1, 1, 2, 1, 2, 1, 1, 0, 1, 1, 2, 1, 2, 1, 1],
    [3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3], [1, 4, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 4, 1],
    [1, 1, 4, 1, 1, 2, 1, 2, 1, 2, 1, 1, 4, 1, 1], [3, 1, 1, 4, 1, 1, 3, 1, 3, 1, 1, 4, 1, 1, 3],
    [1, 3, 1, 1, 4, 1, 1, 2, 1, 1, 4, 1, 1, 3, 1], [1, 1, 3, 1, 1, 4, 1, 1, 1, 4, 1, 1, 3, 1, 1],
    [5, 1, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 1, 5]
]


class Bag:
    def __init__(self, distribution):
        self.letters = [char for char, count in distribution.items() for _ in range(count)]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.letters)

    def draw_letters(self, count):
        return [self.letters.pop() for _ in range(count) if self.letters]

    def is_empty(self):
        return not self.letters

    def get_remaining_count(self):
        """Retourne le nombre de lettres restantes dans le sac."""
        return len(self.letters)