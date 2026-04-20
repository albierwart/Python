import math

from datetime import datetime, date, time, timedelta

# 
# 
#  nom = input("quel est ton nom? ")
# print(f"bonjour {nom}")

# age_texte = input("quel age as tu?")
# age_int = int(age_texte)
# print(type(age_int))

# faire un programme d imc, on demande le poirds la taille et on affiche l imc(poids/taille*taille)

# poids = float(input("quel est votre poids en kg? "))
# taille = float(input("quel est votre taille en metre? "))
# imc = poids/(taille** 2)
# print(f"votre imc est de {imc:.2f}")

# exercice 1 
# Demander un nombre à l'utilisateur et afficher son double.

# nbr = float(input("Entrez  un nombre: "))
# print(nbr *2)

# Exercice 2 : Convertisseur d'âge

# Demander l'âge en années, afficher l'âge en mois et en jours (365 jours par an).

# age= int(input("quel age as tu: "))
# age_mois = age *12
# age_jour = age*365

# print(f"{age} ans = {age_mois} mois")
# print(f"{age} ans = {age_jour} jours")

# Exercice 3 : La moyenne de deux notes

# Demander deux notes (sur 20), calculer et afficher la moyenne.

# note1 = float(input("note 1 = "))
# note2 = float(input("note 2 = "))
# print(f"la moyenne est : {(note1 + note2)/2}/20")

# Exercice 4 : Périmètre et aire du rectangle

# Demander longueur et largeur, afficher le périmètre et l'aire.

# longeur = float(input("longueur: "))
# largeur = float(input("largueur: "))
# print(f" perimetre : {(longeur+largeur)*2}")
# print(f"aire : {longeur*largeur}")

# Exercice 5 : Calculateur de pourboire

# Demander le montant de l'addition et le pourcentage de pourboire, afficher le pourboire et le total.

# aPayer = float(input("quel est le montant de l'addition "))
# pourcentagePourboire = float(input(" quel est le pourcentage de pourboire que vous voulez laisser "))
# pourboire= aPayer/100*pourcentagePourboire
# print(f"a {pourcentagePourboire} le pourboire est de {pourboire}")
# print(f"le total a payer est de {aPayer + pourboire}")

# Exercice 6 : Secondes en minutes

# Demander un nombre de secondes, afficher combien de minutes et secondes cela représente

# nbrSecondeTotal = int(input("nombre de seconde : "))
# nbrMinute = nbrSecondeTotal//60
# # nbrSeconde = nbrSecondeTotal% 60
# nbrSeconde = nbrSecondeTotal- nbrMinute*60
# print(f"{nbrSecondeTotal} secondes = {nbrMinute} minutes et {nbrSeconde} secondes")

# Exercice 7 : Convertisseur de devises

# Demander un montant en euros et un taux de change, afficher le montant converti.

# euros = float(input("montant en euros : "))
# tauxDeChange = float(input("taux de change: "))
# resultat = euros*tauxDeChange
# print(f"{euros} euros = {resultat:.2f} dollars")

# Exercice 9 : Le répartiteur d'addition

# Demander le montant total d'un repas et le nombre de personnes, afficher la part par personne.

# prixTotal = float(input("montant total de reps : "))
# nbrPers = float(input("cb de pers: "))
# print(f"caque personne paye : {prixTotal/nbrPers} euros")

# Exercice 10 : Calcul du temps de trajet

# Demander une distance (km) et une vitesse (km/h), afficher le temps de trajet en heures et minutes.

# distance = int(input("distance (km) "))
# vitesse = int(input("Vitesse (km/h) : "))
# nbrHeur = distance//vitesse
# nbrMinutes = (distance % vitesse)/80*60
# print(f"temps de trajet : {nbrHeur} heure et {nbrMinutes} minutes")

# Exercice 11 : Le volume d'une piscine

# Demander longueur, largeur et profondeur d'une piscine (en mètres), afficher le volume en m³ et en litres.

# longueur = float(input("longueur : "))
# largeur = float(input("largeur : "))
# profondeur = float(input("profondeur : ")) 
# volume = longueur*largeur*profondeur
# litres = volume*1000
# print(f""" 
#       volume : {volume} m³
#       soit {litres} litres""")                

# Exercice 12 : Le temps d'attente

# Demander une année de naissance et l'année courante, afficher l'âge et dire dans combien d'années la personne aura 100 an

# birthYears = int(input("annee de naissance : "))
# CurrentYears = int(input("annee courante"))
# age = CurrentYears-birthYears
# to100Years = 100-age
# print(f""" 
# vous avez {age} ans
# il vous reste {to100Years} ans avant d avoir 100 ans""")

# Exercice 13 : Le prix après réduction

# Demander le prix initial d'un produit et le pourcentage de réduction, afficher le montant de la réduction et le prix final.

# initPrice = float(input(" prix initial : "))
# reduction = float(input(" pourcentage de reduction : "))
# print(f" reduction = {initPrice/100*20:.2f} euros")
# print(f"prix final = {initPrice-(initPrice/100*20)} euros")

# Exercice 14 : La vitesse moyenne

# Demander une distance (km) et un temps (heures et minutes séparément), afficher la vitesse moyenne en km/h.

# distance = int(input("istance(km) : "))
# heure = int(input("heure : "))
# minutes = int(input("minutes : "))
# nbrMinuteTotal = heure*60 + minutes
# moyenne = distance / nbrMinuteTotal * 60
# print(f"Vitessse moyenne {moyenne:.2f} km/heure")

# Exercice 15 : Le carré d'un nombre

# Demander un nombre, afficher son carré et sa racine carrée.
# nombre = int(input("entrerz un nombre : "))
# carre = nombre ** 2
# racineCarree = nombre ** 0.5
# print(f"""
# le carre de {nombre} est {carre}
# la racine carrée de {nombre} est {racineCarree:.2f} """)

# Exercice 16 : Le périmètre et l'aire du cercle

# Demander le rayon d'un cercle, afficher son périmètre (circonférence) et son aire.

# Formules :

#     Périmètre = 2 × π × rayon

#     Aire = π × rayon²
# Utilisez : import math puis math.pi pour la valeur de π
# (Périmètre) = D (Diamètre) x π, soit D x 3,14.
#  aire = pi *r²

# rayon = int(input("rayon : "))
# perimetre =  (rayon+rayon) * math.pi
# aire = math.pi * (rayon**2)
# print(f""" 
# perimetre : {perimetre:.2f} cm
# aire : {aire:.2f} cm²""")

# Exercice 18 : Le temps de téléchargement

# Demander la taille d'un fichier (Mo) et la vitesse de connexion (Mo/s), afficher le temps de téléchargement en secondes.

# taille = int(input("taille du fichier (Mo) : "))
# vitesse = int(input("vitesse (Mo/s)"))
# print(f"temps de telechargement = {taille/vitesse:.2f} secondes")

# Exercice 19 : Le taux d'alcoolémie simplifié

# Demander le nombre de verres bus et le poids (kg). Afficher le taux d'alcoolémie approximatif.

# Formule simplifiée : taux = (nombre_verres × 10) / (poids × 0.7)

# nbrVerres = int(input("nombre de verre : "))
# poids = int(input("poids (kg) : "))
# print(f"taux approximatif : {(nbrVerres*10)/(poids*0.7):.2f} g/l")

# maintenant = datetime.now()
# aujourdhui = date.today()

# print(maintenant)
# print(aujourdhui)