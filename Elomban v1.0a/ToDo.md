# ✅ TODO — Elomban | Scrab v1.0b

## ✔️ Fait jusqu’à présent :

### 🎮 Structure du Projet & Mécanique
- [x] `main.py` fonctionnel (initialisation Pygame et boucle de jeu principale).
- [x] **Architecture modulaire** fonctionnelle (`main.py` + `modules/`).
- [x] **`settings.py`** : Constantes globales (chemins, couleurs, tailles...).
- [x] **`config/*.ini`** : Fichiers de configuration propres et lus correctement au démarrage.
- [x] **`tile.py` & `letter.py`** : Classes `Sprite` fonctionnelles et intégrées.
- [x] **`player.py`** : Classe `Player` gérant un nom, un score et une main de **8 lettres**.
- [x] **`rules.py`** : Définit la distribution et les points des lettres Douala, la pioche (`Bag`).
- [x] **`ui.py`** : Gestionnaire d'interface pour afficher les infos de jeu sur l'écran.

### 🖼️ Visuel & Fonctionnalité
- [x] Affichage de la grille 15x15 via un `sprite.Group`.
- [x] Chargement de l'**image de fond** du plateau et du **chevalet**.
- [x] Une **vraie partie démarre** : joueurs créés, 8 lettres distribuées depuis la pioche.
- [x] La main du joueur actuel s'affiche correctement en bas de l'écran.
- [x] Le panneau d'informations s'affiche à droite de l'écran.

---

## 🔜 À faire (prochaines étapes par ordre de priorité) :

### 1. 🕹️ Interactivité Principale (Le Gameplay !)
- [ ] **Implémenter le Drag & Drop :**
    - [ ] Gérer `MOUSEBUTTONDOWN` pour saisir une `Letter` de la main.
    - [ ] Gérer `MOUSEMOTION` pour que la lettre suive la souris.
    - [ ] Gérer `MOUSEBUTTONUP` pour poser la lettre sur une `Tile` valide (ou la faire revenir à la main).

### 2. 🧠 Logique & Règles du Tour
- [ ] **`button.py` :** Créer la classe `Button` et afficher "Valider", "Échanger", "Passer".
- [ ] **Logique des Boutons :**
    - [ ] Lier le bouton "Valider" à une fonction `terminer_tour()`.
- [ ] **Logique de Validation dans `rules.py`** (à appeler depuis `terminer_tour()`) :
    - [ ] **Placement :** 1er mot au centre, mots suivants connectés.
    - [ ] **Dictionnaire :** Charger le dictionnaire Douala et valider les mots formés.
    - [ ] **Score :** Calculer les points (valeur des lettres + cases bonus + bonus Scrabble).
- [ ] **Gestion des Tours :** Mettre à jour le joueur (`current_player`), repiocher des lettres.

### 3. ✨ Polissage & Améliorations
- [ ] **`layers.py` :** Si besoin, formaliser la gestion des calques pour le rendu.
- [ ] Ajouter une police de caractères Douala pour un meilleur rendu visuel des textes.
- [ ] Afficher dynamiquement le score potentiel pendant qu'on place les lettres.
- [ ] Animation ou feedback visuel/sonore au placement d'une lettre.

### 4. 🚀 Déploiement & Finalisation
- [ ] **Sauvegarde / Chargement :** Gérer les fichiers de sauvegarde XML/XSD.
- [ ] **`requirements.txt` :** Lister les dépendances (pygame, etc.).
- [ ] Création d'un exécutable `PyInstaller`.
- [ ] Tests sur Windows & Linux.