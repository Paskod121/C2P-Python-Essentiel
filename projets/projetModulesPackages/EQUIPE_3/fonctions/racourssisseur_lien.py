import requests

def run_shortener():
    print("\n=== Raccourcisseur de lien ===")
    # Saisie du lien par l'utilisateur
    url = input("Lien à raccourcir : ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Lien invalide. Il doit commencer par http:// ou https://")
        return
    try:
        response = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=5)
        if response.status_code == 200:
            print(f"Lien court : {response.text}")
        else:
            print("Erreur API is.gd")
    except Exception as e:
        print("Erreur réseau ou API indisponible")
        