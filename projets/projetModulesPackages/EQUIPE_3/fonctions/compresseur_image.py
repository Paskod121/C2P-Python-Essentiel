from PIL import Image

def run_compressor():
    print("\n=== Compresseur d’image ===")
    input_path = input("Entrée : ").strip()
    output_path = input("Sortie (défaut : out.jpg) : ").strip() or "out.jpg"
    try:
        quality = int(input("Qualité (1–95, défaut : 60) : ").strip() or "60")
        if not (1 <= quality <= 95):
            quality = 60
    except:
        quality = 60
    if not input_path:
        print("Chemin de fichier vide.")
        return
    try:
        img = Image.open(input_path)
        img.save(output_path, optimize=True, quality=quality)
        print(f"Image compressée : {output_path}")
    except Exception as e:
        print("Erreur de compression ou fichier introuvable")
