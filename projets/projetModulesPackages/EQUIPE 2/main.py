# importation du package
from manita import ocr,img_compressor,raccourcisseur_url, scanner, qrcmaker

# Fonction menu
def menu() :
    print("\n\nMENU – Modules & Packages")
    print("=" * 40)
    print("1. Scanner WiFi (Windows)")
    print("2. OCR (image -> texte)")
    print("3. Générateur de QR Code")
    print("4. Raccourcisseur de lien")
    print("5. Compresseur d’image")
    print("0. Quitter\n\n")

    choix = input("Votre choix :")
    return choix

# Principal
while True:
    choice = menu()

    if choice == "1" :
        scanner.scanner_wifi()
    elif choice == "2" :
        ocr.run_ocr()
    elif choice == "3" :
        qrcmaker.qr()
    elif choice == "4" :
         raccourcisseur_url.run_raccourcisseur_url()
    elif choice == "5" :
        img_compressor.run_img_compressor()
    else :
        break