from fonctions.fonctionalites import *

mon_nom = input("Bienvenue.Veuillez entrer votre nom : ")

def main(user_name):
    menu()
    choix = input("🔀 Entrez le numéro de la fonctionnalité que vous souhaitez utiliser : ")
    while choix != "0":
        if choix == "1":
            run_wifi()

        elif choix == "2":
            try:
                chemin_image = input("Entrez le chemin de l'image : ").strip().strip('"')
                run_ocr(chemin_image)
            except FileNotFoundError :
                print("❌ Fichier introuvable")

        elif choix == "3":
            element = input("Données à mettre dans le QR code (texte ou lien) : ").strip()
            nom = input("Nom du fichier QR (ex: mon_qr.png) : ").strip()
            if element:
                generer_qr(element, nom)
            else:
                print("❌ Données vides !")

        elif choix == "4":
            url = input("Entrez le lien à raccourcir : ").strip()
            if url.startswith("http" or "https"):
                racourcisseur(url)
            else:
                print("❌ Lien invalide !")

        elif choix == "5":
            chemin = input("Chemin de l'image (ex: photo.jpg): ").strip('"')
            nom = input("Nom de sortie (ex: out.jpg) : ").strip()
            try:
                qualite = int(input("Qualité (1-95) : "))
                if 1 <= qualite <= 95:
                    compresseur(chemin, nom, qualite)
                else:
                    print("⚠ Qualité hors des limites !")
            except ValueError:
                print("❌ Qualité invalide !")

        else:
            print("🚫 Choix invalide veuillez réessayer !")
        menu()
        choix = input("🔀 Entrez le numéro de la fonctionnalité que vous souhaitez utiliser : ")

    print(f"\nMerci {user_name} d'avoir utilisé ce programme. Au revoir 👋")

main(mon_nom)