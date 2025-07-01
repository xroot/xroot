from os import path

# Définition des chemins principaux
path_log = path.abspath('../log/scrabble.log')
path_icon = path.abspath('../assets/images/icon/Scrabble_launcher.ico')
path_background = path.abspath('../assets/images/background/')
path_buttons = path.abspath('../assets/images/assets/buttons/primary/')
path_letters = path.abspath('../assets/images/assets/letters/')
path_tiles = path.abspath('../assets/images/assets/tiles/')
path_music = path.abspath('../assets/sounds/')

def get_language_paths(ui_language):
    if ui_language == 'english':
        return 0, path.abspath('../assets/images/assets/buttons/primary/english/')
    elif ui_language == 'french':
        return 1, path.abspath('../assets/images/assets/buttons/primary/french/')
    else:
        return 0, path.abspath('../assets/images/assets/buttons/primary/english/')