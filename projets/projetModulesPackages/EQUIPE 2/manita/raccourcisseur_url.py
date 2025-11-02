# Importation des biblio et modules nécessaires
import requests

# fonction d'accueil
def message():
    print("=== RACCOURCISSEUR D'URL ===")

# Fonction de vérification saisie et effectue le traitement
def run_raccourcisseur_url():
    message()
    try:
        while True :
            get_url =  str(input("Entrer le lien (commençant par http:// ou https://) : "))

            if not get_url.startswith(( "http://", "https://")):    # Vérifie que l'URL commence par http:// ou https://
                print("L'URL doit commencer par http:// ou https://")

            # Appel API is.gd pour créer le lien raccourci
            new_url = requests.get(f"https://is.gd/create.php?format=simple&url={get_url}").text
            # .text fourni le contenu de la réponse HTTP sous forme de chaîne de caractères
            print(f"L'URL raccourci est : {new_url}")
            break

    except Exception as e:
        print(f"Une erreur s'est produite :{e}")