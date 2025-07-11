import cv2
# import face_recognition # Commenté pour éviter les erreurs d'importation
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, Qt
from tools.ui_loader import load_ui
from services import recognition_service


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

        self.known_face_encodings = []
        self.known_face_names = []

        self.frame_scaling = 0.5

        # Initialiser le détecteur de visages de OpenCV
        # Assure-toi que le fichier haarcascade_frontalface_default.xml est accessible
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def start_camera(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)

        if self.cap.isOpened():
            self.known_face_names, self.known_face_encodings = recognition_service.load_known_faces()
            self.timer.start(30)
            print("INFO: Caméra principale démarrée et prête pour la détection (reconnaissance simulée).")
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

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, 1.1, 4)

        for (x, y, w, h) in faces:
            # Pour l'instant, la reconnaissance est simulée
            name = "Inconnu"

            # Si tu réactives face_recognition, tu pourrais faire la comparaison ici:
            # face_roi = rgb_small_frame[top:bottom, left:right]
            # face_encoding = face_recognition.face_encodings(face_roi)[0]
            # matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.6)
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = self.known_face_names[first_match_index]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.rectangle(frame, (x, y + h - 35), (x + w, y + h), (255, 255, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (x + 6, y + h - 6), font, 1.0, (0, 0, 0), 1)

            # Afficher le résultat en console
            print(f"Visage détecté : {name}")

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
