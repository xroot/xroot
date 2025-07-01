"""
Module de lecture et parsing des fichiers de configuration Elomban.
Lit les fichiers INI/text pour l'affichage, les règles du jeu, l'UI et les joueurs.
Expose : h_display_params, h_rules_params, h_ui_params, players
"""

import re
from os import path

# ~~~~~~~~ Variables retournées ~~~~~~~~
h_display_params = {}
h_rules_params = {}
h_ui_params = {}
players = []

# ~~~~~~~~ Helpers ~~~~~~~~
def str_to_bool(s):
    """Convertit une chaîne en booléen Python."""
    if s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    else:
        raise ValueError(f"Cannot convert {s} to a bool")

# ~~~~~~~~ Chemins relatifs ~~~~~~~~
PATH_CONF_DISPLAY = path.abspath('../config/display_settings.ini')
PATH_CONF_RULES = path.abspath('../config/game_settings.ini')
PATH_CONF_UI = path.abspath('../assets/texts/ui_content.ini')

# ~~~~~~~~ Regex utiles ~~~~~~~~
match_word = re.compile(r'^([a-z_]*)\s*=\s*([A-Za-z]*)\s*$')
match_integer = re.compile(r'^([a-z_]*)\s*=\s*([0-9]*)\s*$')
match_names = re.compile(r'^([a-z_]*)\s*=([^0-9])*$')
match_ui_word = re.compile(r'([a-z_]*)\s*=\s*([éA-Za-z12<>\'/\s:.!_]*)\s*')

# ~~~~~~~~ Lecture display_settings.ini ~~~~~~~~
try:
    with open(PATH_CONF_DISPLAY, "r", encoding="utf8") as f:
        for line in f:
            word_found = match_word.search(line)
            int_found = match_integer.search(line)

            if word_found:
                param = str(word_found.group(1))
                value = str_to_bool(word_found.group(2))
                if param in {
                    'fullscreen', 'resizable', 'resolution_auto', 'enable_windows_ten_upscaling',
                    'enable_hardware_accelerated', 'enable_double_buffer'
                }:
                    h_display_params[param] = value

            if int_found:
                param = str(int_found.group(1))
                if param == 'custom_window_height':
                    h_display_params[param] = int(int_found.group(2))
                if param == 'max_fps':
                    h_display_params[param] = int(int_found.group(2))
except FileNotFoundError:
    print(f"[Config] Fichier non trouvé: {PATH_CONF_DISPLAY}")

# ~~~~~~~~ Lecture game_settings.ini ~~~~~~~~
try:
    with open(PATH_CONF_RULES, "r", encoding="utf8") as f:
        for line in f:
            word_found = match_word.search(line)
            int_found = match_integer.search(line)
            names_found = match_names.search(line)

            if word_found:
                param = str(word_found.group(1))
                if param in {
                    'display_next_player_hand', 'display_type_of_tile_on_hoovering',
                    'display_new_score_in_real_time'
                }:
                    h_rules_params[param] = str_to_bool(word_found.group(2))
                elif param in {'letters_language', 'ui_language'}:
                    h_rules_params[param] = str(word_found.group(2))

            if names_found:
                param = str(names_found.group(1))
                if param == 'players_names':
                    start = line.index('=') + 1
                    string_names = line[start:]
                    names = string_names.strip().split(' ')
                    players.extend([name for name in names if name.strip()])

            if int_found:
                param = str(int_found.group(1))
                if param == 'number_of_letters_per_hand':
                    h_rules_params[param] = int(int_found.group(2))
except FileNotFoundError:
    print(f"[Config] Fichier non trouvé: {PATH_CONF_RULES}")

# ~~~~~~~~ Lecture ui_content.ini ~~~~~~~~
ui_possible_values = (
    'current_player_turn', 'next_player_hand', 'scores', 'player_score', 'previous_turn_summary',
    'word_and_points', 'scrabble_obtained', 'nothing_played', 'remaining_letters', 'remaining_letter',
    'no_remaining_letter', 'double_letter', 'triple_letter', 'double_word', 'triple_word'
)

try:
    with open(PATH_CONF_UI, "r", encoding="utf8") as f:
        for line in f:
            text_found = match_ui_word.search(line)
            if text_found:
                param = str(text_found.group(1))
                if param in ui_possible_values:
                    start = line.index('=') + 1
                    all_values = line[start:]
                    values_array = [value.strip() for value in all_values.strip().split('/') if value.strip()]
                    h_ui_params[param] = values_array
except FileNotFoundError:
    print(f"[Config] Fichier non trouvé: {PATH_CONF_UI}")