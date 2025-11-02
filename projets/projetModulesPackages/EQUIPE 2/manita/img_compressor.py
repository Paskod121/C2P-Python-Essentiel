# Importation des biblio et modules nécessaires
from PIL import Image
# fonction d'accueil
def message():
    print("=== IMAGE COMPRESSOR ===")

# Fonction qui récupère la qualité de l'image
def quality():
    try:
       qlty = int(input("Entrer la qualité de l'image compressée [1 - 95] : "))
       if 1 <= qlty <= 95:
           qlty = qlty
       else:
           qlty = 60
       return qlty
    except ValueError:
        print(f"Saisie invalide. ")


# Fonction de vérification saisie et effectue le traitement
def run_img_compressor():
    message()
    try:
        image_path = str(input("Entrer le chemin de l'image : "))

        qualite = quality()

        img = Image.open(image_path)  # pour ouvrir l'image
        img.save(image_path, "JPEG", quality= qualite)       # compression
        img.show()          # Affichage image

    except FileNotFoundError:
        print("Ce fichier n'existe pas")

    except Exception as e:
        print(f"Une erreur s'est produite :{e}")


