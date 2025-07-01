# graphics.py

import pygame
import os
from modules.settings import ACTIVE_LANGUAGE, ASSET_PATH

# Dictionnaire des lettres chargées (Douala)
letters_images = {}


def load_board_background():
    path = os.path.join(ASSET_PATH, "background", "empty_background.png")
    return pygame.image.load(path).convert()


def load_letter_images():
    global letters_images
    letter_path = os.path.join(ASSET_PATH, "letters", ACTIVE_LANGUAGE)
    for filename in os.listdir(letter_path):
        if filename.endswith(".png"):
            letter = os.path.splitext(filename)[0].upper()
            img = pygame.image.load(os.path.join(letter_path, filename)).convert_alpha()
            letters_images[letter] = img


def get_letter_image(letter):
    return letters_images.get(letter.upper())
