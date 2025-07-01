# Fichier : main.py
import pygame
from configparser import ConfigParser

# On importe les modules clés de notre application
from modules.game_logic import Game
from modules.display import DisplayManager
from modules.settings import GREEN_BOARD


def load_display_config():
    """
    Charge la configuration d'affichage depuis config/display_settings.ini
    """
    parser = ConfigParser()
    try:
        parser.read('config/display_settings.ini', encoding='utf-8')
        config = {
            'fullscreen': parser.getboolean('Window', 'fullscreen', fallback=False),
            'width': int(parser.getfloat('Resolution', 'custom_window_height', fallback=720) * (16 / 9)),
            'height': parser.getint('Resolution', 'custom_window_height', fallback=720)
        }
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier de config : {e}")
        # Configuration de secours
        config = {'fullscreen': False, 'width': 1280, 'height': 720}

    return config


def main():
    """
    Fonction principale qui initialise et lance le jeu.
    """
    pygame.init()

    # 1. Charger la configuration de l'affichage
    display_config = load_display_config()

    # 2. Créer la fenêtre Pygame avec les bons paramètres
    flags = pygame.DOUBLEBUF | pygame.RESIZABLE
    if display_config['fullscreen']:
        flags |= pygame.FULLSCREEN

    screen = pygame.display.set_mode((display_config['width'], display_config['height']), flags)
    pygame.display.set_caption("Elomban")

    # 3. Créer le gestionnaire d'affichage qui calcule TOUTES les dimensions
    display_manager = DisplayManager(screen)

    # 4. Créer l'instance du jeu en lui passant l'écran ET le gestionnaire de dimensions
    game = Game(screen, display_manager)

    # --- BOUCLE DE JEU PRINCIPALE ---
    clock = pygame.time.Clock()
    while game.running:
        # Gérer les événements utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            # Passer les événements à la logique du jeu pour qu'elle les traite
            #game.handle_event(event)

        # Mettre à jour l'état du jeu
        game.update()

        # Effacer l'écran précédent
        screen.fill((GREEN_BOARD ))  # Fond noir par défaut

        # Dessiner la nouvelle frame
        game.draw()

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter la vitesse du jeu à 60 images par seconde
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()