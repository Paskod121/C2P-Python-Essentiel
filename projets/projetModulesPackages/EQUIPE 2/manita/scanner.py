# Les importations
import subprocess


def scanner_wifi():
    """
    Affiche un message d'accueil, demande une confirmation et lance le scan
    des réseaux Wi-Fi via 'netsh wlan show networks' si l'utilisateur confirme.
    """
    # aceuil
    print()
    print("Scanner wifi")
    print("-" * 12)
    print()

    # --- Ajout de l'option de confirmation (y/n) ---
    confirmation = input("Voulez-vous lancer le scan des réseaux Wi-Fi ? (y/n) : ").lower()

    if confirmation == 'y':
        print("\nScaning...")
        print()

        # Execution de la commande netsh wlan show networks
        try:
            # Note : L'encodage cp850 est souvent nécessaire pour les sorties netsh en français sur Windows
            reseau = subprocess.run(
                ['netsh', 'wlan', 'show', 'networks'],
                capture_output=True,
                text=True,
                encoding="cp850"
            )

            # Affichage du résultat
            print(reseau.stdout)

        except FileNotFoundError:
            # Se produit si 'netsh' n'est pas trouvé (rare sur Windows, mais bonne pratique)
            print("Erreur: La commande 'netsh' n'a pas été trouvée. Assurez-vous d'utiliser Windows.")
        except Exception as erreur:
            print("Erreur inattendue lors de l'exécution : ", erreur)

    else:
        print("\nOpération annulée par l'utilisateur.")