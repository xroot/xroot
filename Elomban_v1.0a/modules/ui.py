import pygame

from modules.settings import BOARD_DIMENSION, DELTA

class UIManager:
    """
    Gère l'affichage de toutes les informations textuelles de l'interface.
    Toutes ses dimensions et positions sont calculées dynamiquement.
    """

    def __init__(self, screen, display_manager):
        self.screen = screen
        self.display_manager = display_manager

        tile_size = self.display_manager.tile_size

        try:
            self.font_title = pygame.font.SysFont("calibri", int(tile_size * 0.55), bold=True)
            self.font_normal = pygame.font.SysFont("calibri", int(tile_size * 0.45))
        except pygame.error:
            self.font_title = pygame.font.SysFont("arial", int(tile_size * 0.55), bold=True)
            self.font_normal = pygame.font.SysFont("arial", int(tile_size * 0.45))

        self.color_title = (255, 255, 255)
        self.color_text = (220, 220, 220)
        self.panel_bg = (40, 50, 70, 230)  # fond translucide (RGBA, alpha ignoré si pas de surface convert_alpha)

        self.start_x = self.display_manager.zone_jeu_width + int(tile_size * DELTA)
        self.start_y = self.display_manager.board_offset_y
        self.line_spacing = int(tile_size * 0.7)
        self.panel_width = 340

    def draw_game_info(self, player, bag):
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

    def draw_welcome_panel(self):
        """
        Affiche le panneau d'accueil (menu principal) à droite lors du lancement du jeu.
        """
        header = "Elomban | Scrab v1.0a - Buña bwà bwàm"
        menu_items = [
            "Nouveau jeu",
            "Charger une partie",
            "High scores",
            "Options",
            "Règles du jeu",
            "Quitter"
        ]

        x = self.start_x
        y = self.start_y

        # --- Fond du panneau ---
        panel_height = self.line_spacing * (2 + len(menu_items)) + 60
        panel_rect = pygame.Rect(x - 10, y - 10, self.panel_width, panel_height)
        pygame.draw.rect(self.screen, (40, 50, 70), panel_rect, border_radius=10)

        # --- Titre (header) ---
        text_surface = self.font_title.render(header, True, self.color_title)
        self.screen.blit(text_surface, (x + 10, y))
        y += self.line_spacing + 10

        # --- Séparateur visuel ---
        pygame.draw.line(self.screen, (180, 180, 180), (x + 10, y), (x + self.panel_width - 20, y), 2)
        y += 20

        # --- Items du menu ---
        for item in menu_items:
            text_surface = self.font_normal.render(f"▶ {item}", True, self.color_text)
            self.screen.blit(text_surface, (x + 20, y))
            y += self.line_spacing