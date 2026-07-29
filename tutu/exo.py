
# # exo 1
# def Saluer(nom, age):
#     print(f"Bonjour {nom}, vous avez {age} ans.")
# Saluer("alain", 32)

# # exo 2

# def produit(a,b):
#     if a==0 or b==0:
#         print("multiplication par zero detectee")
#         return 0
#     else:
#         return a * b

# exo 3

# carre = []

# for nb in range(1,11):
#     carre.append(nb*nb)

# print(carre)
# #  puis refaites-le en une ligne avec une compréhension de liste. demander un cour

# exo 4

# voyelle = ["a", "e", "i", "o", "u", "y"]

# def compter_voyelle(texte):
#     cpt = 0
#     for letter in texte:
#         if letter in voyelle:
#             cpt +=1
#     return cpt

# print(compter_voyelle("Python"))

# exo 5

# for nb in range(1,21):
#     if nb%3 == 0:
#         print("fizz")
#     elif nb % 5 == 0:
#         print("buzz")
#     else:
#         print(nb)

# exo 6

# def inverser(texte):
#     mot_inverse = ""
#     for lettre in texte:
#         mot_inverse = lettre + mot_inverse
#     print(mot_inverse)

# # exo 7 

# def convertir_en_fahrenheit(liste_celsius):
#     liste_fahrenheit = []
#     for nb in liste_celsius:
#         liste_fahrenheit.append(nb * (9/5) + 32)
#     print(liste_fahrenheit)

# # exo 8 

# # def maximun(a,b,c):
# #     if a > b and a > c:
# #         return a
# #     elif b > c:
# #         return b
# #     else:
# #         return c

# # exo 9

# def nombre_de_mots(texte):
# #     mots = texte.split()
#     return len(mots)

# Exercice 1 : L'Inspecteur des Données
# Écrivez une fonction analyser_conteneur(conteneur) qui prend une liste, un tuple, un set ou un dict.

#     Affiche le type du conteneur.

#     Si c'est une liste, un tuple ou un set, affiche l'élément ayant la plus grande valeur.

#     Si c'est un dictionnaire, affiche la clé associée à la valeur maximale.

# Testez avec [10, 20, 5], {"a": 1, "b": 8, "c": 4} et {5, 15, 0}.

# def analyser_conteneur(conteneur):
#     typ = type(conteneur)
#     print(typ)
#     if typ == list or typ == set or typ == tuple:
#         print(f"valeur max = {max(conteneur)}")
#     elif typ == dict:
#         cle_max = max(conteneur, key=conteneur.get)
#         print(f"clé max = {cle_max}, valeur = {conteneur[cle_max]}")

# analyser_conteneur({"a": 1, "b": 8, "c": 4})

# Exercice 2 : La Compagnie de Transport
# Trajets : trajets = [("Paris", "Lyon", 480), ("Lyon", "Marseille", 315), ("Paris", "Nantes", 385), ("Bordeaux", "Toulouse", 245)]

#     Fonction distance_totale_ville(liste_trajets, ville) qui retourne la distance totale des trajets partant de cette ville.

#     Une compréhension de liste pour obtenir toutes les villes de départ uniques, triées par ordre alphabétique.

# def distance_totale_ville(liste_trajets, ville):
#     distanceTotal = 0
#     for ville1, ville2, distance in liste_trajets:
#         if ville1 == ville:
#             distanceTotal += distance
#     print(f"distance totale = {distanceTotal}")

# trajets = [("Paris", "Lyon", 480), ("Lyon", "Marseille", 315), ("Paris", "Nantes", 385), ("Bordeaux", "Toulouse", 245)]
# distance_totale_ville(trajets, "Paris")

# demander a deepseek la theorie et une serie d exercice sur  compréhension de liste car je ne sais rien dessus

# Exercice 3 : Le Détecteur de Palindromes Amélioré
# Fonction est_palindrome(phrase) qui :

#     Nettoie la chaîne (garde uniquement les lettres).

#     Convertit en minuscules.

#     Vérifie si c'est un palindrome.

#     Utilise une boucle for... else pour afficher le résultat, sans variable booléenne.

# Testez avec "Engage le jeu que je le gagne" et "Python est amusant".

# def est_palindrome(texte):
#     texte_propre = ""
#     for char in texte:
#         if char.isalpha():
#             texte_propre += char
#     texte_minuscule = texte_propre.lower()
#     i = 0
#     for i in range(len(texte_minuscule)//2):
        
#         if texte_minuscule[nb] <= texte_minuscule[len(texte_minuscule)-1-i]:
#             print("ceci n est pas un palindrome")
#             break
        
#     else:
#         print("ceci est un palindrome")

# Exercice 4 : L'Analyseur de Logs
# Créez un fichier server.log avec des lignes comme :
# text

# 2023-10-27 10:15:21 INFO Utilisateur connecté
# 2023-10-27 10:15:25 WARNING Espace disque faible
# 2023-10-27 10:15:30 ERROR Échec de l'écriture en base
# 2023-10-27 10:16:01 INFO Données envoyées

# Lisez ce fichier et créez un dictionnaire stats comptant les occurrences de chaque niveau (INFO, WARNING, ERROR). Utilisez .get().





# Exercice 5 : Mini-Gestionnaire de Bibliothèque
# Modélisez une bibliothèque comme un dictionnaire {titre: nb_exemplaires}.

#     emprunter(bibliotheque, titre) : décrémente de 1 si dispo, sinon lève ValueError.

#     rendre(bibliotheque, titre) : incrémente de 1, ou ajoute le livre avec 1 exemplaire.

# Testez le scénario :

#     {"1984": 2, "Le Meilleur des Mondes": 0}

#     Empruntez "1984", rendez-le.

#     Empruntez "Le Meilleur des Mondes" (doit lever une exception).

#     Empruntez "Fondation" (doit lever une exception).

#     Rendez "Fondation", puis empruntez-le.

# Exercice 6 : Défi de Compréhension
# Sans exécuter, quelle est la valeur finale de resultat ?

