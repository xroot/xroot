# modules/ui.py

import pygame

# On importe les "plans" (constantes de design) depuis notre source unique de vérité.
from modules.settings import BOARD_DIMENSION, DELTA


class UIManager:
    """
    Gère l'affichage de toutes les informations textuelles de l'interface.
    Toutes ses dimensions et positions sont calculées dynamiquement.
    """

    def __init__(self, screen, display_manager):
        """
        Initialise le gestionnaire d'UI.

        Args:
            screen (pygame.Surface): La surface principale sur laquelle dessiner.
            display_manager (DisplayManager): L'objet qui a déjà calculé toutes les dimensions.
        """
        self.screen = screen
        self.display_manager = display_manager

        # --- On récupère les dimensions dynamiques depuis le DisplayManager ---
        # C'est la solution à ton "tile_size = TILE_SIZE ??????"
        # On ne l'importe plus, on la récupère de l'objet qui l'a calculée.
        tile_size = self.display_manager.tile_size

        # --- Polices de caractères dynamiques ---
        # Leur taille dépend maintenant de la taille réelle des tuiles.
        try:
            self.font_title = pygame.font.SysFont("calibri", int(tile_size * 0.55), bold=True)
            self.font_normal = pygame.font.SysFont("calibri", int(tile_size * 0.45))
        except pygame.error:
            self.font_title = pygame.font.SysFont("arial", int(tile_size * 0.55), bold=True)
            self.font_normal = pygame.font.SysFont("arial", int(tile_size * 0.45))

        # --- Couleurs ---
        self.color_title = (255, 255, 255)
        self.color_text = (220, 220, 220)

        # --- Calcul de position dynamique ---

        # C'est la solution à ton "BOARD_COLS //// lui aussi * tile_size"
        # On utilise la constante BOARD_DIMENSION (qui vaut 15) et on la multiplie
        # par la taille réelle d'une tuile pour obtenir la largeur en pixels.
        grid_width_pixels = BOARD_DIMENSION * tile_size

        # La marge à droite est aussi dynamique.
        margin_right = DELTA * tile_size

        self.start_x = self.display_manager.board_offset_x + grid_width_pixels + margin_right
        self.start_y = self.display_manager.board_offset_y
        self.line_spacing = int(tile_size * 0.7)

    def draw_game_info(self, player, bag):
        """
        Dessine toutes les informations de jeu pour le tour actuel.
        """

        player_hand_str = ', '.join(sorted([l.character for l in player.hand.sprites()]))
        info_lines = [
            f"Tour de : {player.name}",
            f"Score : {player.score}",
            "",
            "Main du Joueur :",
            player_hand_str,
            "",
            f"Pioche : {bag.get_remaining_count()} lettres"
        ]

        for i, line in enumerate(info_lines):
            is_title = (i == 0)
            font_to_use = self.font_title if is_title else self.font_normal
            color_to_use = self.color_title if is_title else self.color_text

            text_surface = font_to_use.render(line, True, color_to_use)
            text_rect = text_surface.get_rect(topleft=(self.start_x, self.start_y + i * self.line_spacing))

            self.screen.blit(text_surface, text_rect)
