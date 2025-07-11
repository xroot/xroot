import os
import cv2
from pathlib import Path

FACES_DIR = Path("data/faces")
FACES_DIR.mkdir(parents=True, exist_ok=True)


def save_face_image(name, image):
    person_dir = FACES_DIR / name.strip().lower().replace(" ", "_")
    person_dir.mkdir(exist_ok=True)

    existing_files = len(list(person_dir.glob("*.jpg")))
    image_path = person_dir / f"{existing_files + 1}.jpg"

    cv2.imwrite(str(image_path), image)
    print(f"Image sauvegardée pour \'{name}\' sous \'{image_path}\'")
    return str(image_path)


def list_faces():
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
