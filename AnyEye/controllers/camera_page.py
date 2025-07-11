# controllers/camera_page.py (mis à jour pour la reconnaissance)

import cv2
import face_recognition
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, Qt
from tools.ui_loader import load_ui
from services import faces_storage

class CameraPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = load_ui("ui/camera_page.ui")
        if not self.ui:
            return

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        self.cap = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        # --- NOUVEAU : Préparation pour la reconnaissance ---
        self.known_face_encodings = []
        self.known_face_names = []
        
        # On réduit la taille des images pour accélérer le traitement
        self.frame_scaling = 0.5 # Traiter des images 2x plus petites

    def start_camera(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
        
        if self.cap.isOpened():
            # --- NOUVEAU : Charger les visages connus au démarrage de la caméra ---
            self.known_face_encodings, self.known_face_names = faces_storage.load_known_faces()
            self.timer.start(30)
            print("INFO: Caméra principale démarrée et prête pour la reconnaissance.")
        else:
            self.ui.videoFeedLabel.setText("Erreur: Impossible d'accéder à la caméra.")
            print("ERREUR: Caméra principale non accessible.")

    def stop_camera(self):
        self.timer.stop()
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            print("INFO: Caméra principale arrêtée.")

    def update_frame(self):
        if self.cap is None or not self.cap.isOpened():
            return
            
        ret, frame = self.cap.read()
        if not ret:
            return

        # --- MODIFIÉ : Boucle de reconnaissance ---
        # 1. Redimensionner l'image pour un traitement plus rapide
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_scaling, fy=self.frame_scaling)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # 2. Détecter tous les visages dans l'image actuelle
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Voir si le visage correspond à un visage connu
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.6)
            name = "Inconnu"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
            
            face_names.append(name)

        # 3. Dessiner les résultats sur l'image originale (pas la petite)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Remettre les coordonnées à l'échelle de l'image originale
            top = int(top / self.frame_scaling)
            right = int(right / self.frame_scaling)
            bottom = int(bottom / self.frame_scaling)
            left = int(left / self.frame_scaling)

            # Dessiner un rectangle autour du visage
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)

            # Dessiner une étiquette avec le nom
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 255, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)
        
        # --- Fin de la modification ---

        # Convertir l'image finale (avec les dessins) pour l'affichage
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        
        self.ui.videoFeedLabel.setPixmap(pixmap.scaled(
            self.ui.videoFeedLabel.size(), 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        ))

    def showEvent(self, event):
        super().showEvent(event)
        self.start_camera()

    def hideEvent(self, event):
        super().hideEvent(event)
        self.stop_camera()