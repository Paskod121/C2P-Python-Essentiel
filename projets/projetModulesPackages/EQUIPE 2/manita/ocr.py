# Importation des biblio et modules nécessaires

from PIL import Image
import  pytesseract as tess

# fonction d'accueil

def message():
    print("=== OCR (Image --> Texte) ===")

# Fonction de vérification saisie et effectue le traitement
def run_ocr():
    message()
    try:
        image_path = str(input("Entrer le chemin de l'image : "))

        while True:

            image = Image.open(image_path)  # pour ouvrir l'image

            # Convertir en niveaux de gris
            image = image.convert('L')

            # Appliquer le seuillage (Threshold, binarisation)
            # Ici, 128 est la valeur seuil (toute valeur en dessous devient noir, au-dessus devient blanc)
            image = image.point(lambda x: 0 if x < 180 else 255, '1')

            text = tess.image_to_string(image)  # converti le texte en chaine de caractères

            if text.strip() == "":
                print("Aucun texte détecté.")
                break
            else:
                print("_" * 45)
                print(text)
                print("_" * 45)
                break

    except FileNotFoundError:
       print("Ce fichier n'existe pas")

    except Exception as e:
       print(f"Une erreur s'est produite :{e}")