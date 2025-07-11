# ToDo List - AnyEye v1.0

---
# Étape 1 : Finaliser le MVP (Minimum Viable Product)
---

## 1.1. Implémenter la Logique de Reconnaissance Faciale
# C'est le CŒUR du projet. Actuellement, on détecte des visages, on ne les reconnaît pas.

- [ ] **Dans `services/faces_storage.py` (ou un nouveau `recognition_service.py`) :**
    - [ ] Créer une fonction `load_known_faces()` qui, au démarrage :
        - Lit toutes les images dans le dossier `/data/faces/`.
        - Utilise `face_recognition.face_encodings()` pour calculer le vecteur de 128 dimensions pour chaque visage.
        - Stocke ces encodages en mémoire (ex: un dictionnaire `{'nom': [encodage], ...}`).
- [ ] **Dans `controllers/camera_page.py` :**
    - [ ] Dans la boucle `update_frame`, après avoir détecté des visages (`face_recognition.face_locations()`):
        - Calculer les encodages des visages détectés dans le flux live.
        - Utiliser `face_recognition.compare_faces()` pour comparer chaque visage live avec les encodages connus.
        - Si une correspondance est trouvée, récupérer le nom associé.
    - [ ] **Dans la partie UI (OpenCV) :**
        - Dessiner un rectangle autour des visages reconnus.
        - Écrire le nom de la personne reconnue sous le rectangle.
        - Afficher "Inconnu" si aucune correspondance n'est trouvée.

## 1.2. Construire la Page "Historique"
# Maintenant qu'on peut reconnaître, on peut logger les événements.

- [ ] **Conception UI :** Créer `ui/history_page.ui` avec une `QTableWidget` (colonnes : Timestamp, Nom, Miniature) et un bouton "Effacer l'historique".
- [ ] **Logique de stockage :**
    - [ ] Choisir une méthode de stockage :
        - **Simple :** Fichier JSON ou CSV.
        - **Robuste :** Base de données SQLite (`data/history.db`).
- [ ] **Contrôleur :** Créer `controllers/history_page.py`.
    - [ ] Dans `camera_page.py`, quand un visage est reconnu, envoyer un signal ou appeler une fonction pour enregistrer l'événement (timestamp, nom, et une petite image du visage).
    - [ ] Dans `history_page.py`, créer une fonction `refresh_history()` qui lit la base de données/fichier et remplit la `QTableWidget`.

---
# Étape 2 : Améliorations et Fiabilisation
---

- [ ] **Gestion des Erreurs :**
    - [ ] Que se passe-t-il si aucune caméra n'est détectée au lancement ? Afficher un message clair à l'utilisateur.
- [ ] **Performance :**
    - [ ] La reconnaissance faciale peut être lente et geler l'UI. Déplacer la boucle de traitement d'image (OpenCV + face_recognition) dans un `QThread` séparé pour garder l'interface fluide.
- [ ] **Configuration Externe :**
    - [ ] Créer un fichier `config.ini` ou `config.json` pour gérer :
        - L'index de la caméra (0, 1, ...).
        - Les URLs pour les caméras IP.
        - Le seuil de tolérance pour la reconnaissance faciale.
- [ ] **Page "Paramètres" :**
    - [ ] Créer l'UI et le contrôleur pour permettre à l'utilisateur de modifier les valeurs du fichier de configuration.

---
# Étape 3 : Fonctionnalités Futures (Post-MVP)
---

- [ ] **Support des Caméras IP :**
    - [ ] Dans la page Paramètres, permettre à l'utilisateur d'ajouter/supprimer des URLs de flux vidéo.
    - [ ] Modifier les contrôleurs de caméra pour qu'ils puissent utiliser soit un index local (`cv2.VideoCapture(0)`), soit une URL (`cv2.VideoCapture("http://...")`).
- [ ] **Système d'Alertes :**
    - [ ] Intégrer une bibliothèque pour envoyer des notifications (email, Telegram, ou Twilio comme prévu initialement).
    - [ ] Dans la page Paramètres, configurer les détails de l'alerte (destinataire, etc.).
- [ ] **Packaging pour Distribution :**
    - [ ] Finaliser le fichier `setup.py` pour la publication sur PyPI.
    - [ ] Créer un exécutable autonome avec `PyInstaller` ou `cx_Freeze`.
- [ ] **Sécurité :**
    - [ ] Implémenter le chiffrement de la base de données des visages et de l'historique.