# services/faces_storage.py

import os
import cv2
import face_recognition
from pathlib import Path

# Chemin vers le dossier où les visages sont stockés
FACES_DIR = Path("data/faces")

# S'assurer que le dossier de données existe
FACES_DIR.mkdir(parents=True, exist_ok=True)

def save_face_image(name, image):
    """
    Sauvegarde l'image d'un visage pour une personne donnée.
    Crée un sous-dossier par personne pour stocker plusieurs images.
    """
    person_dir = FACES_DIR / name.strip().lower().replace(" ", "_")
    person_dir.mkdir(exist_ok=True)
    
    # Compter combien d'images existent déjà pour trouver le prochain numéro
    existing_files = len(list(person_dir.glob("*.jpg")))
    image_path = person_dir / f"{existing_files + 1}.jpg"
    
    cv2.imwrite(str(image_path), image)
    print(f"Image sauvegardée pour '{name}' sous '{image_path}'")
    return str(image_path)

def list_faces():
    """
    Liste toutes les personnes et le nombre d'images associées.
    Retourne un dictionnaire: {'nom_personne': [liste_chemins_images]}
    """
    faces = {}
    if not FACES_DIR.exists():
        return faces
        
    for person_dir in FACES_DIR.iterdir():
        if person_dir.is_dir():
            name = person_dir.name.replace("_", " ").title()
            images = [str(p) for p in person_dir.glob("*.jpg")]
            if images:
                faces[name] = images
    return faces

# --- NOUVELLE FONCTION : Le cerveau de la reconnaissance ---
def load_known_faces():
    """
    Charge tous les visages connus depuis le dossier /data/faces.
    Calcule les encodages pour chaque visage.
    
    Retourne:
        - known_face_encodings (list): Une liste des encodages de 128 dimensions.
        - known_face_names (list): Une liste des noms correspondants.
    """
    known_face_encodings = []
    known_face_names = []
    
    print("Chargement des visages connus...")
    
    registered_faces = list_faces()
    
    for name, image_paths in registered_faces.items():
        for image_path in image_paths:
            try:
                # Charger l'image
                face_image = face_recognition.load_image_file(image_path)
                
                # Calculer l'encodage. On suppose une seule personne par photo.
                # face_encodings renvoie une liste, on prend le premier élément.
                face_encodings_list = face_recognition.face_encodings(face_image)
                
                if face_encodings_list:
                    encoding = face_encodings_list[0]
                    known_face_encodings.append(encoding)
                    known_face_names.append(name)
                    print(f"  - Encodage chargé pour {name} depuis {os.path.basename(image_path)}")
                else:
                    print(f"  - AVERTISSEMENT: Aucun visage trouvé dans {image_path} pour {name}.")

            except Exception as e:
                print(f"ERREUR lors du chargement de {image_path}: {e}")

    print(f"{len(known_face_encodings)} encodages de visages connus chargés.")
    return known_face_encodings, known_face_names