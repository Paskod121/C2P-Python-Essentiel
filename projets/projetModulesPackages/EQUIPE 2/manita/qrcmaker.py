import qrcode


def acceuille_message ():
    print("Bienvenu dans le generateur du Code QR")

    print("="*38)
def qr () :
    acceuille_message()
    try :
        while True :
            saisi_qr = input("Veuillez Entrer un lien :")

            cod = qrcode.QRCode(version = 1, box_size = 9, border = 3)
            cod.add_data(saisi_qr)
            cod.make(fit = True)

            img = cod.make_image(fill_color = "black",back_color = "white")

            img.save("codeqr.png")

            print("code QR generé avec succès !")
            break
    except Exception as u :
        print(f"Une erreur s'est produite:{u}")