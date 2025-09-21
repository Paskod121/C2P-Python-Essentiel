print("🎓Calculateur de Notes - Système Educatif Togolais TG")
print("="*50)
print("\n👤INFORMATIONS ETUDIANT")
nom = input("Nom et Prénoms de l'élève : ")
ma_classe = input("Classe (ex: 3ème, 2nd, 1ère, Tle) : ")
ets = input("Etablissement : ")
print("\n📚SAISIE DES NOTES DU TRIMESTRE (sur 20)")
math = float(input("📐Mathématiques : "))
francais = float(input("📝Français : "))
anglais = float(input("🇬🇧 Anglais : "))
physique = float(input("⚗️Sciences Physiques : "))
svt = float(input("🧬SVT : "))
histo_geo = float(input("🌍Histoire-Géographie : "))
print("="*50)
print(f"📊BULLETIN SCOLAIRE - {nom}")
print(f"🏫{ets} - {ma_classe}")
print("="*50)
print("\n📚NOTES DU TRIMESTRE : ")
print(f"📐Mathématiques       : {math}/20 (écart: {math - 10})")
print(f"📝Français            : {francais}/20 (écart: {francais - 10})")
print(f"🇬🇧 Anglais             : {anglais}/20 (écart: {anglais - 10})")
print(f"⚗️Sciences Physiques  : {physique}/20 (écart: {physique - 10})")
print(f"🧬SVT                 : {svt}/20 (écart: {svt - 10})")
print(f"🌍Histoire-Géographie : {histo_geo}/20 (écart: {histo_geo - 10})")
print("\n📊 RESULTATS GENERAUX : ")
total_points = math + francais + anglais + physique + svt + histo_geo
moyenne = total_points/6
print(f"📈 Moyenne générale : {moyenne:.2f}/20")
print(f"📋 Totals de points : {total_points}/120")
print("\n✅VALIDATION DES MATIERES (>= 10/20) :")
if math >= 10:
    print("📐Mathématiques : True")
else:
    print("📐Mathématiques : False")
if francais >= 10:
    print("📝Français : True")
else:
    print("📝Français : False")
if anglais >= 10:
    print("🇬🇧 Anglais : True")
else:
    print("🇬🇧 Anglais : False")
if physique >= 10:
    print("⚗️Sciences Physiques : True")
else:
    print("⚗️Sciences physiques : False")
if svt >= 10:
    print("🧬SVT : True")
else:
    print("🧬SVT : False")
if histo_geo >= 10:
    print("🌍Histoire-Géographie : True")
else:
    print("🌍Histoire-Géographie : False")
print("\nANALYSES PEDAGOGIQUES :")
if math >= 10 and francais >= 10:
    print("📚Matières fondementales validées (Math et Français) : True")
else:
    print("📚Matières fondementales validées (Math et Français) : False")
if math >= 10 and francais >= 10 and anglais >= 10 and physique >= 10 and svt >= 10 and histo_geo >= 10:
    print("🏆Toutes matières validées : True")
else:
    print("🏆Toutes matières validées : False")
if math >= 10 or francais >= 10 or anglais >= 10 or physique >= 10 or svt >= 10 or histo_geo >= 10:
    print("⭐Au moins une matière validée : True")
else:
    print("⭐Au moins une matière validée : False")
moyenne_scientifique = (math + physique + svt)/3
moyenne_litteraire = (francais + anglais + histo_geo)/3
if moyenne_scientifique > moyenne_litteraire:
    print("🔬Profil Scientifique : True")
    print("📖Profil littéraire : False")
    print("⚖️Profil équilibré : False")
elif moyenne_scientifique < moyenne_litteraire:
    print("🔬Profil Scientifique : False")
    print("📖Profil littéraire : True")
    print("⚖️Profil équilibré : False")
else:
    print("🔬Profil Scientifique : False")
    print("📖Profil littéraire : False")
    print("⚖️Profil équilibré : True")
print("\n🏅MENTIONS ET DECISIONS : ")
if moyenne >= 16:
    print("🌟Mention TRES BIEN (>= 16) : True")
else:
    print("🌟Mention TRES BIEN (>= 16) : False")
if moyenne >= 14:
    print("⭐Mention BIEN(>= 14) : True")
else:
    print("⭐Mention BIEN(>= 14) : False")
if moyenne >= 12:
    print("✨Mention ASSEZ BIEN(>= 12) : True")
else:
    print("✨Mention ASSEZ BIEN(>= 12) : False")
if moyenne >= 10:
    print("✅Admis en classe supérieure(>= 10) : True")
else:
    print("✅Admis en classe supérieure(>= 10) : False")
if moyenne < 10:
    print("❌Echec(< 10) : True")
else:
    print("❌Echec(< 10) : False")
print("\n🥇MATIERE DOMINANTE : ")
if math > (francais and anglais and physique and svt and histo_geo):
    print("📐Mathématiques en tête: True")
else:
    print("📐Mathématiques en tête: False")
if francais > (math and anglais and physique and svt and histo_geo):
    print("📝Français en tête: True")
else:
    print("📝Français en tête: False")
if anglais > (francais and math and physique and svt and histo_geo):
    print("🇬🇧 Anglais en tête: True")
else:
    print("🇬🇧 Anglais en tête: False")
if physique > (francais and anglais and math and svt and histo_geo):
    print("⚗️Sciences Physiques en tête: True")
else:
    print("⚗️Sciences Physiques en tête: False")
if svt > (francais and anglais and physique and math and histo_geo):
    print("🧬SVT en tête: True")
else:
    print("🧬SVT en tête: False")
if histo_geo > (francais and anglais and physique and svt and math):
    print("🌍Histoire-Géographie en tête: True")
else:
    print("🌍Histoire-Géographie en tête: False")
print("\n : ")
print(f"📊 Points pour la moyenne (10/20) : {10 - moyenne :.2f}")
print(f"✨ Points pour Assez Bien (12/20) : {12 - moyenne :.2f}")
print(f"⭐ Points pour Bien (14/20) : {14 - moyenne :.2f}")
print(f"🌟 Points pour Très Bien (16/20) : {16 - moyenne :.2f}")
print("\n🚀 POTENTIEL D'AMÉLIORATION :")
print(f"📐 Maths : {20 - math} points possibles")
print(f"📝 Français : {20 - francais} points possibles")
print(f"🇬🇧 Anglais : {20 - anglais} points possibles")
print(f"⚗️ Sciences Physiques: {20 - physique} points possibles")
print(f"🧬 SVT : {20 - svt} points possibles")
print(f"🌍 Histoire-Géographie : {20 - histo_geo} points possibles")
print("\n🇹🇬 Bulletin établi selon le système éducatif togolais")
print("🎓 Bon courage Paskod pour la suite de tes études !")
print("💪 Travaille dur pour réussir ton parcours scolaire !")