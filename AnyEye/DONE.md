# Rapport d'Avancement - AnyEye v1.0 (Style xRootMiel)

On a bien avancé, brother ! Le projet a pris forme et les fondations sont maintenant solides et modulaires. Voici le récapitulatif de ce qui est en place.

---

## ✅ Ce qui est Terminé et Fonctionnel

*   **Architecture du Projet (MVC)**
    *   Structure de dossiers claire (`controllers`, `models`, `services`, `tools`, `ui`) prête à évoluer.

*   **Fenêtre Principale et Navigation**
    *   Chargement de la fenêtre principale (`main_window.ui`).
    *   Application du thème global `dark.qss` (la touche xRootMiel !).
    *   Mise en place d'un système de navigation par pages avec `QStackedWidget`.
    *   Les boutons du menu (`Caméra`, `Visages`, etc.) changent correctement la page affichée.

*   **Gestion Modulaire des Pages (UI)**
    *   Création d'un chargeur d'UI robuste (`tools/ui_loader.py`) pour éviter les conflits de noms et les problèmes de chemin.

*   **Page "Caméra" (Vue Principale)**
    *   Création de l'interface `camera_page.ui`.
    *   Création du contrôleur `camera_page.py`.
    *   Affiche le flux vidéo en direct.

*   **Page "Gestion des Visages"**
    *   Création de l'interface `face_manager.ui`.
    *   Création du contrôleur `face_manager.py`.
    *   Affiche un flux vidéo pour la prévisualisation.
    *   Fonctionnalité de capture d'image et d'ajout d'un visage avec un nom.
    *   (Simulation de) Sauvegarde des visages via le service `faces_storage`.
    *   Affiche la liste des visages enregistrés.

*   **Gestion Optimisée des Ressources**
    *   La caméra de chaque page s'active **uniquement** lorsque la page devient visible (`showEvent`).
    *   La caméra se désactive automatiquement lorsque la page est cachée (`hideEvent`), libérant ainsi les ressources.

---

## ⏳ Ce qui est en Cours / Partiellement Implémenté

*   **Service de Stockage (`faces_storage`)** : Le service est appelé, mais la logique de stockage des "encodages" de visage (les données mathématiques pour la reconnaissance) n'est pas encore implémentée. Pour l'instant, on ne fait que sauvegarder l'image.
*   **Pages "Historique" et "Paramètres"** : Elles existent en tant que widgets vides dans `main.py` pour que la navigation fonctionne, mais elles n'ont ni interface ni logique.

Le projet est passé d'une idée à une application de bureau fonctionnelle avec une navigation et une gestion des ressources propres. Prochaine étape : le cerveau de la reconnaissance !