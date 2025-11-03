from PIL import Image
import pytesseract

def run_ocr():
    print("\n=== OCR (image -> texte) ===")
    path = input("Fichier : ")
    lang = input("Langue OCR (ex: fra) [Entrée pour défaut] or eng: ").strip()
    if not path:
        print("Chemin de fichier vide.")
        return
    try:
        img = Image.open(path)
        text = pytesseract.image_to_string(img, lang=lang)
        if text.strip():
            print("Texte détecté :\n" + text.strip())
        else:
            print("Aucun texte détecté")
    except Exception as e:
        print("Erreur OCR ou fichier introuvable")