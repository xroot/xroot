import os
#import face_recognition

def load_known_faces():
    known_face_encodings = []
    known_face_names = []
    faces_dir = "data/faces"

    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)
        print(f"Dossier {faces_dir} créé. Veuillez y ajouter des images de visages connus.")
        return known_face_names, known_face_encodings

    for person_name in os.listdir(faces_dir):
        person_dir = os.path.join(faces_dir, person_name)
        if os.path.isdir(person_dir):
            for filename in os.listdir(person_dir):
                if filename.lower().endswith((".jpg", ".png", ".jpeg")):
                    image_path = os.path.join(person_dir, filename)
                    try:
                        # Ici, tu devras intégrer la logique de chargement d'image et d'encodage
                        # avec face_recognition. Pour l'exemple, nous allons simuler.
                        # image = face_recognition.load_image_file(image_path)
                        # encodings = face_recognition.face_encodings(image)
                        # if encodings:
                        #     known_face_encodings.append(encodings[0])
                        #     known_face_names.append(person_name)
                        #     print(f"Chargé {person_name} de {image_path}")
                        # else:
                        #     print(f"Aucun visage trouvé dans {image_path}")

                        # Simulation pour le moment
                        print(f"Simulons le chargement de {person_name} de {image_path}")
                        known_face_names.append(person_name)
                        known_face_encodings.append([0] * 128)  # Encodage bidon pour la simulation

                    except Exception as e:
                        print(f"Erreur lors du chargement de {image_path}: {e}")
    return known_face_names, known_face_encodings
