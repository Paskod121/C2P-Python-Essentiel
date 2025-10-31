# Variables globales
nombre_total_inscrits = 0
frais_de_base = 0
effectif_6eme = 0
effectif_5eme = 0
effectif_4eme = 0
effectif_3eme = 0
effectif_2nde = 0
effectif_1ere = 0
effectif_tle = 0
recettes_totales = 0
nbre_aucune = 0
nbre_famialiale = 0
nbre_sociale = 0
nbre_excel = 0
bourse = "aucun"
global nom, prenom, age, classe, etablissement, reduction,frais_base

# Fonction d'affichage du menu
def menu():
    print("\nBienvenue dans le menu du gestionnaire d'inscription scolaire.\n")
    print("GESTIONNAIRE D'INSCRIPTION SCOLAIRE")
    print("="*40)
    print("1. Inscrire un élève")
    print("2. Consulter l'élève actuel")
    print("3. Modifier les informations")
    print("4. Calculer les frais")
    print("5. Voir les statistiques")
    print("6. Quitter")

# Fonction pour Inscription avec paramètre par défaut
def inscrire_eleve():
    global nom, prenom, age, classe, etablissement, bourse
    global nombre_total_inscrits,classe

    nom = verificator("Nom de l'élève :",str )
    prenom = verificator("Prenom de l'élève :" ,str)
    age = verificator("L'âge de l'élève :", int)
    while True:
        classe = verificator("La classe de l'élève :(6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Tle) :", str)
        if classe.lower() in ("6ème", "5ème", "4ème", "tle", "3ème", "2nde", "1ère",):
            break
        else: print("❌Saisi invalide. Réessayez svp")
        # verifie si la classe peut accepter un nouveau élève
        disponibilite = verifier_disponibilite()
        if disponibilite :
            nombre_total_inscrits += 1
        else:
            print("Effectif maximal déjà atteint.")
    while True:
        etablissement = verificator("Etablissement (public, privé, technique) :", str)
        if etablissement.lower() in ("privé", "public", "technique"):
            break
        else: print("❌Saisi invalide. Réessayez svp")
    while True:
        bourse = verificator("Type de bourse (excellence, sociale, familiale, aucune) :" , str)
        if bourse.lower() in ("excellence", "sociale", "familiale", "aucune"):
            break
        else: print("❌Saisi invalide. Réessayez svp")

# Fonction pour afficher l'élève actuel
def donnee_eleve():
    global bourse, etablissement
    frais = calculer_frais()
    status  = "Inscrit" if classe else "Non inscrit"
    print("CONSULTATION DE L'ÉLÈVE ACTUEL")
    print("="*40)
    print(f"Nom :{nom}")
    print(f"Prenom :{prenom}")
    print(f"Age :{age} ans")
    print(f"Classe :{classe}")
    print(f"Etablissement :{etablissement}")
    print(f"Bourse :{bourse}")
    print(f"Frais :{frais}")
    print(f"Status :{status}")


# Fonction pour modifier les donnees de l' etudiant
def modif_info():
    global nom, prenom, age, classe, etablissement, bourse
    print("MODIFICATION DES INFORMATIONS")
    print("="*40)
    print(f"Nom actuel : {nom}")
    nom = verificator("Nouveau nom : ",str)
    print(f"Prenom actuel : {prenom}")
    prenom = verificator("Nouveau prenom : ",str)
    print(f"Age actuel : {age} ans")
    age = verificator("Nouveau age : ",int)
    print(f"Classe actuel : {classe}")
    while True:
        try:
         classe = input("Nouvelle classe : ")
         if classe.lower() in ("6ème", "5ème","tle", "4ème", "3ème", "2nde", "1ère" ):
             break
        except ValueError:
            print("❌Saisi invalide. Réessayez svp")
    print(f"Etablissement actuel : {etablissement}")
    while True:
        try:
            etablissement = input("Nouvel etablissement : ")
            if etablissement.lower() in ("privé", "public", "technique"):
                break
        except ValueError:
            print("❌Saisi invalide. Réessayez svp")
    print(f"Type de bourse actuel : {bourse}")
    while True:
        try:
            bourse = input("Nouveau type de bourse : ")
            if bourse.lower() in ("excellence", "sociale", "familiale", "aucune"):
                break
        except ValueError:
            print("❌Saisi invalide. Réessayez svp")
    print("\nINFORMATIONS MODIFIEES AVEC SUCCES")

# Fonction de calcul des frais idem quelque soit la classe
def calculer_frais():
    global recettes_totales, frais_base,reduction, bourse, etablissement
    frais_base = 35000 if etablissement == "privé" else 0
    reduction = 0.5 if bourse == "excellence" else 0.3 if bourse == "sociale" else 0.2 if bourse == "familiale" else 0
    frais_final = frais_base * (1 - reduction) + 2000  # + frais APE

    # Mise à jour des recettes
    recettes_totales += frais_final
    return frais_final

# Calcul des frais
def detail_frais():
    global recettes_totales, frais_base, classe , etablissement, bourse

    print("CALCUL DÉTAILLÉ DES FRAIS")
    print("="*40)
    print(f"Classe : {classe}")
    print(f"Etablissement : {etablissement}")
    print(f"Type de bourse : {bourse}")
    print()
    print("DETAIL DES FRAIS")
    print(f"- Frais de base : {frais_base}")
    print(f"- Réduction bourse ({reduction*100}%) : -{frais_base*reduction}")
    print(f"- Frais APE : 2000FCFA")
    print(f"- Cantine : 1000FCFA")
    print("- Frais transport : 1500FCFA")
    print(f"- Total à payer : {frais_base*(1- reduction) +4500}FCFA")

# Fonction pour afficher les statistiques
def affichage_stats():
    global effectif_6eme, effectif_5eme, effectif_4eme,effectif_3eme,effectif_2nde, effectif_1ere, effectif_tle
    global nbre_excel,nbre_sociale,nbre_famialiale,nbre_aucune
    # met à jour les effectifs de chaque classe
    effectif_6eme = update_effectif_6eme()
    effectif_5eme = update_effectif_5eme()
    effectif_4eme = update_effectif_4eme()
    effectif_3eme = update_effectif_3eme()
    effectif_2nde = update_effectif_2nde()
    effectif_1ere = update_effectif_1ere()
    effectif_tle = update_effectif_tle()
    # met à jour le nbre de boursiers
    nbre_sociale = update_nbre_sociale()
    nbre_excel = update_nbre_excel()
    nbre_famialiale = update_nbre_familiale()
    nbre_aucune = update_nbre_aucune()

    print("STATISTIQUES GÉNÉRALES")
    print("="*40)
    print("Effectif par classe :")
    print(f"- 6ème : {effectif_6eme} élèves")
    print(f"- 5ème : {effectif_5eme} élèves")
    print(f"- 4ème : {effectif_4eme} élèves")
    print(f"- 3ème : {effectif_3eme} élèves")
    print(f"- 2nde : {effectif_2nde} élèves")
    print(f"- 1ère : {effectif_1ere} élèves")
    print(f"- Terminale : {effectif_tle} élèves")
    print()
    print(f"Recettes totales {recettes_totales}:")
    print("Repartition des bourses :")
    print(f"- Excellence : {nbre_excel} élèves")
    print(f"- Sociale : {nbre_sociale} élèves")
    print(f"- Familiale : {nbre_famialiale} élèves")
    print(f"- Aucune : {nbre_aucune} élèves")

# update nombre boursier fonctions
def update_nbre_aucune():
    global nbre_aucune,bourse
    if bourse.lower() == "aucune":
        nbre_aucune += 1
    return nbre_aucune

def update_nbre_familiale():
    global nbre_famialiale,bourse
    if bourse.lower() == "familiale":
        nbre_famialiale += 1
    return nbre_famialiale

def update_nbre_sociale():
    global nbre_sociale,bourse
    if bourse.lower() == "sociale":
        nbre_sociale += 1
    return nbre_sociale

def update_nbre_excel():
    global nbre_excel,bourse
    if bourse.lower() == "excellence":
        nbre_excel += 1
    return nbre_excel

# Fonction de vérification de la saisi utilisateur
def verificator(messages, typ ):
    while True:
        try:
            retour = typ(input(messages))
            return retour
        except ValueError:
            print("❌Saisi invalide. Réessayez svp")


# Mise à jour effectif
def update_effectif_6eme():
    global effectif_6eme, classe
    if classe.lower() == "6ème":
        effectif_6eme += 1
    return effectif_6eme

def update_effectif_5eme():
    global effectif_5eme, classe
    if classe.lower() == "5ème":
        effectif_5eme += 1
    return effectif_5eme

def update_effectif_4eme():
    global effectif_4eme, classe
    if classe.lower() == "4ème":
        effectif_4eme += 1
    return effectif_4eme

def update_effectif_3eme():
    global effectif_3eme, classe
    if classe.lower() == "3ème":
        effectif_3eme += 1
    return effectif_3eme

def update_effectif_2nde():
    global effectif_2nde, classe
    if classe.lower() == "2nde":
        effectif_2nde += 1
    return effectif_2nde

def update_effectif_1ere():
    global effectif_1ere, classe
    if classe.lower() == "1ère":
        effectif_1ere += 1
    return effectif_1ere

def update_effectif_tle():
    global effectif_tle, classe
    if classe.lower() == "tle":
        effectif_tle += 1
    return effectif_tle


#  vérification de disponibilité
def verifier_disponibilite():
    global classe
    dispo = True

    if classe.lower == "6ème":
        dispo = effectif_6eme < 45
    elif classe.lower == "5ème":
        dispo = effectif_5eme < 45
    elif classe.lower == "4ème":
        dispo = effectif_4eme < 45
    elif classe.lower == "3ème":
        dispo = effectif_3eme < 45
    elif classe.lower == "2nde":
        dispo = effectif_2nde < 45
    elif classe.lower == "1re":
        dispo = effectif_1ere < 45
    elif classe.lower == "Tle":
        dispo = effectif_tle < 45
    return dispo




# Fonction qui dirige tout ou persque tout
def maestro():
    while True:
        menu()
        while True:
            try:
                choix = int(input("\nVotre choix : "))
                break
            except ValueError:
                print("Entrer un nombre 1 à 7 selon le menu :")
        if choix == 1 :
            inscrire_eleve()
        elif choix == 2 :
            donnee_eleve()
        elif choix == 3 :
            modif_info()
        elif choix == 4 :
            detail_frais()
        elif choix == 5 :
            affichage_stats()
        else:
            message()
            break

def message():
    print("Merci d'avoir utilisé le gestionnaire d'inscription !")

# mon main
maestro()