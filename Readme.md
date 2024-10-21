# INSPECTOR-IMAGE

## Description:
Ce code combine les fonctionnalités d'extraction des informations GPS à partir des métadonnées EXIF d'une image et la recherche d'un bloc de clé PGP caché dans le contenu binaire de l'image. Il utilise la bibliothèque exifread pour lire les données EXIF et une simple recherche de motifs pour détecter un bloc de clé PGP.

## Explication du code :
### Fonction ```extract_gps_info```:
- Ouvre une image et utilise exifread pour lire les métadonnées.
- Cherche les balises GPS (GPS GPSLatitude, GPS GPSLatitudeRef, GPS GPSLongitude, GPS GPSLongitudeRef).
- Si elles sont présentes, les coordonnées sont converties en degrés décimaux grâce à convert_to_degrees.
### Fonction ```convert_to_degrees```:
- Prend en entrée une valeur GPS sous forme de degrés, minutes, secondes et la référence (N/S pour latitude, E/W pour longitude).
- Convertit cette valeur en degrés décimaux pour une meilleure lisibilité.
### Fonction extract_steganography :
- Lit le fichier image sous forme binaire.
- Cherche les marqueurs de début et de fin d'un bloc PGP (```-----BEGIN PGP PUBLIC KEY BLOCK-----``` et ```-----END PGP PUBLIC KEY BLOCK-----```).
- Si un bloc est trouvé, il est extrait et décodé.
- Renvoie la clé PGP trouvée ou un message indiquant l'absence de clé.
### Fonction main :
- Gère les arguments de la ligne de commande.
- Exécute l'extraction GPS si l'argument est ```-map```.
- Exécute l'extraction de stéganographie si l'argument est ```-steg```.
- Affiche le résultat ou un message d'erreur en cas de commande incorrecte.

## Installation:
- git clone https://learn.zone01dakar.sn/git/mouhameddiouf/inspector-image.git
- pip install exifread

## Utilisation:

- Pour extraire les informations GPS ---> ```python3 decrypt.py -map image.jpeg```
- Pour extraire le message caché (bloc de clé PGP) ---> ```python3 decrypt.py -steg image.jpeg```

## Développeur:
- Prénom Nom: Mouhamed Diouf
- email: seydiahmedelcheikh@gmail.com