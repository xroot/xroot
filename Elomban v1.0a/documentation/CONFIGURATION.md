# Comment utiliser les fichiers de configuration

Ce document explique comment personnaliser les options du jeu via les fichiers de configuration. Chaque fichier comporte déjà des indications, mais ici vous trouverez des détails techniques et des avertissements sur certains effets de bord.

---

## 📺 RÉGLAGES D'AFFICHAGE

**Fichier** : `display_settings.ini`  
Modifiez ce fichier pour adapter l’affichage : résolution, plein écran, rendu graphique, etc.  
*Les valeurs invalides sont ignorées.*

### Fenêtre

- **fullscreen**  
  Bascule entre le mode plein écran et le mode fenêtré.  
  _Valeurs :_ `true` / `false`

- **resizable**  
  (Seulement en mode fenêtré) Permet de redimensionner la fenêtre (toujours au format 16:9).  
  _Valeurs :_ `true` / `false`

- **resolution_auto**  
  Détecte automatiquement la résolution de l’écran.  
  _Avertissement :_ Avec plusieurs écrans, il peut utiliser la résolution totale combinée. Si souci d’affichage, mettez sur `false` et utilisez `custom_window_height`.  
  _Valeurs :_ `true` / `false`

- **custom_window_height**  
  (Quand `resolution_auto` est à `false`)  
  Hauteur de la fenêtre de jeu (format 16:9 imposé). Qualité max : 1920x1080.  
  _Astuce :_ N’utilisez pas une valeur supérieure à la résolution de votre écran.  
  _Exemples :_ `1080` (Full HD), `720` (HD)

- **enable_windows_ten_upscaling**  
  Windows 10 peut forcer certains logiciels à s’afficher à 150%, ce qui peut décaler le jeu hors de l’écran. Désactivez ce comportement uniquement pour ce jeu si besoin (n’affecte pas votre système).  
  _Valeurs :_ `true` / `false`

### Performances

- **enable_hardware_accelerated**  
  Utilise le GPU pour le rendu, améliore les performances.  
  _Avertissement :_ Peut causer des bugs/artefacts sur certains PC.  
  _Valeurs :_ `true` / `false`

- **enable_double_buffer**  
  (Quand l’accélération matérielle est activée)  
  Met en tampon une image pendant que la suivante est générée. Désactivez si vous manquez de mémoire graphique.  
  _Valeurs :_ `true` / `false`

- **max_fps**  
  Limite le nombre d’images par seconde pour réduire la charge système.  
  _Exemples :_ `60`, `50`, `30`

---

## 🎮 PARAMÈTRES DE JEU

**Fichier** : `game_settings.ini`  
Changez la langue, les joueurs et les options d’interface ici.  
*Les valeurs invalides sont ignorées.*

### Langue du jeu

- **letters_language**  
  Définit l’alphabet et les points des lettres du Scrabble.  
  _Valeurs :_ `french` / `english`  
  _Pour personnaliser l’alphabet, les points ou ajouter une langue, modifiez :_ `/sources/letters_and_points.py`

- **ui_language**  
  Définit la langue de l’interface.  
  _Valeurs :_ `french` / `english`  
  _Pour personnaliser les textes UI ou ajouter une langue, modifiez :_ `/config/ui_content.ini`

### Noms des joueurs

- **players_names**  
  Séparez les noms par des ESPACES.  
  Accents, majuscules, chiffres et underscores autorisés.  
  _Max joueurs :_ 6  
  _Longueur max nom :_ 16 caractères  
  _Exemple :_ `Hélène Jonh_Who Tom4 nomorethan16char`

### Options avancées

- **display_next_player_hand**  
  Affiche la main du prochain joueur (pour accélérer le jeu local).  
  _Valeurs :_ `true` / `false`

- **number_of_letters_per_hand**  
  Nombre de lettres par joueur.  
  _Valeurs :_ `5`, `6`, `7`, `8`, `9`

---

## 🚀 Vers une meilleure gestion des options

Un nouveau système plus flexible pour appliquer et gérer les paramètres arrivera bientôt ! Restez à l’écoute pour une expérience personnalisable au top.