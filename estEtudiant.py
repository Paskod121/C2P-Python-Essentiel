# Utilité du programme
print("\n=== Vérificateur d'éligibilité UL ===\n")

#Saisie des informations de l'étudiant
age = int(input("Âge : "))
mention = input("Mention au bac : ")
estInscrit = input("Inscrit à l'UL (oui/non) : ")
nationalite = input("Nationalité : ")

print("\n")
print('--- RÉSULTATS ---')
print("\n")

#Affichage des résultats après vérification

print("Âge <= 22 ans : ", age <= 22)
print("Mention Bien ou Très Bien : ", mention in ("Bien", "Très Bien"))
print("Inscription UL : ", estInscrit == "oui")
print("Nationalité togolaise : ", nationalite == "togolaise")
print("\n")

#Affichage de l'éligibilité générale

print("Éligibilité générale : ", age <= 22 and mention in ("Bien", "Très Bien") and estInscrit == "oui" and nationalite == "togolaise")