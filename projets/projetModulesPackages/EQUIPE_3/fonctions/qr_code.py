import qrcode

def run_qr():
    print("== Générateur de QR ==")

    # On boucle tant que l'utilisateur n'entre rien
    while True:
        try:
            text = input("Veuillez entrer un texte ou un lien: ")

            if not text.strip():  # Entrée vide
                raise ValueError("Le champ ne peut pas être vide.")

            break  # Sortie si l'entrée est valide

        except ValueError as e:
            print(f"Erreur : {e} — Réessayez.\n")

    try:
        # Création du QR code
        cod = qrcode.QRCode(
            version=1,  # Taille du QR (1 = petit, 40 = grand)
            box_size=10,  # Taille des carrés
            border=2  # Bordure blanche autour
        )
        cod.add_data(text)
        cod.make(fit=True)

        # Génération de l'image du QR
        img = cod.make_image(fill_color="green", back_color="white")
        img.save("qr.png")  # Sauvegarde dans le fichier

        print("✅ Code QR généré avec succès !")
        print("📁 Fichier enregistré sous : qr.png")

    except Exception as e:
        print(f"❌ Erreur lors de la génération du QR code : {e}")

