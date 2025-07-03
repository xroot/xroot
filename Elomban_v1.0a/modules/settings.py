# modules/settings.py
import os

"""
Fichier de configuration principal pour les constantes du jeu Elomban.
C'est la source unique de vérité pour les règles de design.
"""

# --- CHEMINS D'ACCÈS ---
# Calcule le chemin racine du projet pour que les accès aux fichiers soient toujours corrects
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_PATH = os.path.join(ROOT_PATH, "assets", "images", "assets")

# --- CONSTANTES DE DESIGN DU PLATEAU ---
# Ces valeurs sont les "plans" de notre interface. Le DisplayManager les utilisera
# pour calculer les dimensions réelles en pixels.
BOARD_DIMENSION = 15  # La grille fait 15x15 tuiles.
DELTA = 1.5  # La marge autour du plateau, exprimée en "unités de tuile".
REFERENCE_TILE_SIZE = 60  # La taille de nos images de tuile de base (qualité de référence).

# --- AUTRES PARAMÈTRES DE JEU ---
FPS = 60
ACTIVE_LANGUAGE = "douala"
NUMBER_OF_LETTERS_PER_HAND = 8

# --- COULEURS (RGB) ---
# Gardons-les ici pour un accès facile
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_BOARD = (22, 128, 131)  # J'ai ajouté ton code couleur ici
