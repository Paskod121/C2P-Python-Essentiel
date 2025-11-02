import subprocess
import qrcode
import pyshorteners
from pytesseract import pytesseract
from PIL import Image
def menu():
    print("""                   ________MENU________\n
                1️⃣- Scanner WI-FI
                2️⃣- OCR ( image en -> texte)    
                3️⃣- Générateur de QR Code
                4️⃣- Racourcisseur de lien        
                5️- Compresseur d'image
                0️⃣- Quitter 🛑 
    """)

def run_wifi():
    print("\n🔍 Scan des réseaux WiFi disponibles...")
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "network"]) # Exécute la commande (netsh wlan show networks)
        print(result.decode("utf-8", errors="ignore")) # Affiche les résultats
    except Exception as e:
        print(f"Erreur : {e}")

def racourcisseur(url):
    try:
        raccourci = pyshorteners.Shortener()
        short_url = raccourci.tinyurl.short(url)   # Raccourcis le lien
        print(f"🔗 Lien raccourci : {short_url}")  # Affiche le lien raccourci
    except Exception as erreur:
        print(f"❌ Erreur : {erreur}")

def compresseur(chemin,nom_img,qualite = 60):
    try:
        image = Image.open(chemin)                          # Cherche l'image
        image.save(nom_img,optimize = True,quality = qualite) # Enrégistre l'image compressée
        print("✅ Image Compressée avec succès !")
    except Exception as erreur:
        print(f"❌ Erreur : {erreur}")

def generer_qr(element,nom):
    try:
        qr = qrcode.QRCode(version = 1, box_size = 8, border = 1)
        qr.add_data(element)                      # Ajout de l'element à afficher après le scan du code qr
        qr.make(fit = True)
        img = qr.make_image(fill_color = "black", back_color = "white")
        img.save(nom)                              # Enrégistre le code qr
        img.show()                                # Affiche un apercu du code qr
        print("✅ Code QR générer avec succès !")
    except Exception as erreur:
        print(f"❌ Erreur : {erreur}")

def run_ocr(chemin_image):
    try:
        chemin_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = chemin_tesseract
        img = Image.open(chemin_image)
        text = pytesseract.image_to_string(img)
        print(f"✅ TEXTE EXTRAIT : {text}")
    except Exception as erreur:
        print(f"❌ Erreur : {erreur}")