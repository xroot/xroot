import pygame
from math import floor

def tiles(value_in_pixels1, value_in_pixels2, tile_size):
    return (round(value_in_pixels1 / float(tile_size)), round(value_in_pixels2 / float(tile_size)))

def tiles1(value_in_pixels, tile_size):
    return (round(value_in_pixels / float(tile_size)))

def pixels(value1_in_tiles, value2_in_tiles, tile_size):
    return ((value1_in_tiles * tile_size), (value2_in_tiles * tile_size))

def solo_pixels(value_in_tiles, tile_size):
    return ((value_in_tiles * tile_size))

def int_pixels(value1_in_tiles, value2_in_tiles, tile_size):
    return (round(value1_in_tiles * tile_size), round(value2_in_tiles * tile_size))

def resize_window(width, height, display_settings):
    # ... (voir code original, retourner la window pygame)
    pass

def log_players_info():
    # ... log sur les joueurs
    pass

def calculate_points(layer_letters_played):
    # ... calcul des points
    return []

def increment_predicted_score():
    # ... incrément du score prédit
    pass