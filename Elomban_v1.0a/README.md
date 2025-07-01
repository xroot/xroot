# 🧩 Elomban | Scrab v1.0a

**Elomban** est une adaptation du jeu de Scrabble jouable localement (hors ligne), en langue **Douala (code : `do`)**. Il s’agit d’un projet éducatif, culturel et ludique, conçu pour valoriser les langues locales à travers le jeu.

---

## 🎯 Objectifs

- Jouer au Scrabble en langue Douala
- Respecter les règles de la langue (lettres spécifiques, orthographe…)
- Interface immersive et fluide
- Multi-joueur local (jusqu’à 6 joueurs)

---

## 📁 Structure du projet
````plaintext
/Elomban/
├── main.py # Point d'entrée du jeu
├── requirements.txt # Dépendances Python
├── README.md # Ce fichier
├── TODO.md # Liste des tâches

├── modules/ # Modules de logique
│ ├── init.py
│ ├── settings.py # Constantes
│ ├── game_logic.py # Moteur du jeu
│ ├── graphics.py # Chargement d’images
│ ├── player.py # Classe joueur
│ ├── config_reader.py # Lecture des fichiers .ini
│ └── ... # Autres modules à venir

├── config/ # Fichiers de configuration
│ ├── game_settings.ini # Réglages du jeu
│ ├── display_settings.ini # Résolution, plein écran, etc.
│ └── langues/ # Traductions par langue

├── assets/ # Images, sons, polices
│ └── images/
│ └── assets/
│ ├── board_background.png
│ ├── buttons/
│ └── letters/
│ └── douala/
│ ├── Ɛ.png, A.png, B.png, ...

├── savegames/ # Parties sauvegardées
│ ├── template_save_game.xml
│ └── template_save_game.xsd
````

---

## 🖥️ Dépendances

- Python ≥ 3.9
- `pygame`

Installe avec :

```bash
pip install -r requirements.txt
```