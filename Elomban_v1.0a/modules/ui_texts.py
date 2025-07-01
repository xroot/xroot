# modules/ui_texts.py

from modules.config_reader import h_ui_params, h_rules_params

# Langue active (ex: 'fr', 'do', 'en')
ui_lang = h_rules_params.get("ui_language", "fr").lower()

# Détermine l'index du texte à afficher selon la langue
lang_map = {
    "fr": 0,
    "do": 0,  # Douala utilise souvent les mêmes index que FR ici
    "en": 1,
    # Ajoute ici d'autres langues si nécessaire
}


def t(key):
    """
    Retourne la chaîne UI correspondant à la clé `key`
    dans la langue active définie dans game_settings.ini.
    """
    index = lang_map.get(ui_lang, 0)
    values = h_ui_params.get(key, ["??"])
    return values[index] if index < len(values) else values[0]
