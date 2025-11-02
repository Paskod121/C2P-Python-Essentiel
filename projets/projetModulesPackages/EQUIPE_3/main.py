from fonctions.menu import *
from fonctions.compresseur_image import *
from fonctions.ocr_Image_text import *
from fonctions.qr_code import *
from fonctions.racourssisseur_lien import *
from fonctions.wifi_scanner import *

while True :
    menu_principal()
    choice = int(input("\nVotre choix : "))
    if choice == 0:
        print("Au revoir.")
        break
    elif choice == 1:
        run_wifi()
    elif choice == 2:
        run_ocr()
    elif choice == 3:
        run_qr()
    elif choice == 4:
        run_shortener()
    elif choice == 5:
        run_compressor()
    else:
        print("Choix invalide. Veuillez entrer un chiffre entre 0 et 5.")
