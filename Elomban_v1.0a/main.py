# Fichier : main.py
import pygame
from configparser import ConfigParser

# On importe les modules clés de notre application
from modules.game_logic import Game
from modules.display import DisplayManager
from modules.settings import GREEN_BOARD
from modules.ui import UIManager


def load_display_config():
    # ... inchangé ...
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
        config = {'fullscreen': False, 'width': 1280, 'height': 720}

    return config


def main():
    pygame.init()

    # 1. Charger la configuration de l'affichage
    display_config = load_display_config()

    # 2. Créer la fenêtre Pygame avec les bons paramètres
    flags = pygame.DOUBLEBUF | pygame.RESIZABLE
    if display_config['fullscreen']:
        flags |= pygame.FULLSCREEN

    screen = pygame.display.set_mode((display_config['width'], display_config['height']), flags)
    pygame.display.set_caption("🧠 Elomban | Scrab v1.0a")

    # 3. Créer le gestionnaire d'affichage qui calcule TOUTES les dimensions
    display_manager = DisplayManager(screen)

    # 4. Créer l'instance du gestionnaire d'UI
    ui_manager = UIManager(screen, display_manager)  # <------ AJOUT

    # 5. Créer l'instance du jeu
    game = Game(screen, display_manager)

    # --- BOUCLE DE JEU PRINCIPALE ---
    clock = pygame.time.Clock()

    etat_jeu = "accueil"  # <------ AJOUT : état du jeu (accueil/menu ou jeu lancé)

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            # Si tu veux plus tard gérer le clic sur "Nouveau jeu", tu pourras changer cet état ici
            # if etat_jeu == "accueil":
            #     ... gestion des clics menu ...
            # else:
            #     game.handle_event(event)

        # Mettre à jour l'état du jeu
        if etat_jeu != "accueil":
            game.update()

        # Effacer l'écran précédent
        screen.fill(GREEN_BOARD)

        # --- Afficher le bon panneau selon l'état ---
        if etat_jeu == "accueil":
            ui_manager.draw_welcome_panel()
        else:
            game.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
