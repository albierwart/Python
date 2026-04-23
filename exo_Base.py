# Exercice 1 : Somme des chiffres

# Calcule la somme des chiffres d'un nombre entier.
# Entrée : 1234
# Sortie : 10 (car 1+2+3+4 = 10)

# nbr = 1234

# somme = 0
# while nbr >0:
#     somme+= nbr%10
#     nbr = nbr//10
# print(somme)
# # -----------------------------------------------------------------------------------------------------
# Exercice 2 : Nombre de chiffres

# Compte combien de chiffres contient un nombre (sans le convertir en string).
# Entrée : 12345
# Sortie : 5

# nbr = 12345

# counter = 0
# while nbr >0:
#     counter+= 1
#     nbr = nbr//10
# print(counter)
# # -----------------------------------------------------------------------------------------------------
# Exercice 3 : Puissance

# Calcule a^b (a puissance b) en utilisant une boucle (sans utiliser **).
# Entrée : a=2, b=5
# Sortie : 32

# def puissance(nombre,puissance):
#     i = 0
#     reponse = 1
#     while i < puissance:
#         reponse = reponse*nombre
#         i+=1
#     return reponse
# print(puissance(2,5))

# # -----------------------------------------------------------------------------------------------------
# Exercice 4 : Table de multiplication

# Affiche la table de multiplication du nombre entré, de 1 à 10, mais uniquement les résultats impairs.
# Entrée : 3
# Sortie : 
# 3 x 1 = 3
# 3 x 3 = 9
# 3 x 5 = 15
# 3 x 7 = 21
# 3 x 9 = 27

# def affTable(nbr):
#     for i in range(1,11):
#         resultat = i*nbr
#         if resultat % 2 != 0:
#             print(f"{nbr} x {i}= {resultat}")
# affTable(3)

# -----------------------------------------------------------------------------------------------------
# Exercice 5 : Moyenne de nombres

# # Demande à l'utilisateur d'entrer des nombres (tape "fin" pour arrêter) et calcule la moyenne.
# Entrée : 10, 20, 30, fin
# Sortie : La moyenne est 20.0

# reponse = 0
# somme = 0
# counter = 0
# boucle = True
# while boucle:
#     reponse = input("entrez un nombre fin pour terminer ")
#     if reponse != "fin":
#         counter+=1
#         somme += int(reponse)
#     else:
#         boucle=False
# print(f"moyenne = {somme/counter}")

# -----------------------------------------------------------------------------------------------------
# Exercice 6 : Recherche dans une liste

# Demande à l'utilisateur de remplir une liste de 5 nombres, puis demande un nombre à rechercher. 
# Affiche "trouvé" ou "non trouvé".
# Entrée liste : [5, 12, 8, 3, 15]
# Entrée recherche : 8
# Sortie : trouvé
# liste = []
# for i in range(0,5):
#     liste.append(int(input("entre un nombre ")))
# cherche= int(input("entre un nombre a chercher dans la liste "))
# if cherche in liste:
#     print("trouve")
# else:
#     print("non trouve")


# # -----------------------------------------------------------------------------------------------------
# # Exercice 7 : Maximum et minimum
# import sys
# # Trouve le maximum et le minimum d'une liste de nombres (sans utiliser max() ni min()).
# # Entrée : [7, 2, 9, 1, 5]
# # Sortie : Maximum = 9, Minimum = 1

# liste = [7, 2, 9, 1, 5]
# min = sys.maxsize
# max = -sys.maxsize
# for i in range(len(liste)):
#     if liste[i] < min:
#         min = liste[i]
#     if liste[i]> max:
#         max = liste[i]
# print (f"max = {max} min = {min}")

# # -----------------------------------------------------------------------------------------------------
# Exercice 8 : Inversion de liste

# Inverse l'ordre d'une liste (sans utiliser reverse() ni [::-1]).
# Entrée : [1, 2, 3, 4, 5]
# Sortie : [5, 4, 3, 2, 1]

# liste = [1,2,3,4,5]
# print(liste)
# for i in range(len(liste)//2):
#     temp = liste[i]
#     liste[i] = liste[len(liste)-1-i]
#     liste[len(liste)-1-i] = temp
# print(liste)

# # -----------------------------------------------------------------------------------------------------
# Exercice 9 : Compteur de voyelles

# Compte le nombre de voyelles (a, e, i, o, u, y) dans une phrase saisie par l'utilisateur.
# Entrée : "Bonjour tout le monde"
# Sortie : 8 voyelles

# listeV = ["a","e","y","u", "i", "o"] 
# texte = input("entrez une phrase ")
# texte = texte.replace(" ", "").lower()
# texte_propre = "".join(c for c in texte if c.isalpha())
# listeTexte = list(texte)
# counter = 0
# for v in listeV:
#     for c in listeTexte:
#         if v == c:
#             counter+=1
# print(f"il y a {counter} voyelle")

# # -----------------------------------------------------------------------------------------------------
# Exercice 10 : Est-ce que la liste est triée ?

# Vérifie si une liste de nombres est triée en ordre croissant.
# Entrée : [1, 3, 5, 7, 9]
# Sortie : True

# Entrée : [1, 5, 2, 7, 9]
# Sortie : False

# liste = [1, 5, 2, 7, 9]

# for i in range(len(liste)-1):
#     if liste[i] > liste[i+1]:
#         print("false")
#         break
# else:
#     print("true")



# # -----------------------------------------------------------------------------------------------------
# Exercice 8 : Somme de deux nombres dans une liste

# Étant donné une liste de nombres et une cible, trouve deux nombres dont la somme égale la cible.
#  Retourne leurs positions ou leurs valeurs.
# # Exemple
# liste = [2, 7, 11, 15]
# cible = 9
# Résultat : (2, 7) ou (0, 1) pour les positions
# liste = [2, 7, 11, 15,1,8]
# cible = 9
# resultat = []
# indices=[]
# for i,v in enumerate(liste):
#     for j,val in enumerate(liste):
#         if v+val == cible:
#             if (v, val) not in resultat and (val, v) not in resultat :
#                 resultat.append((v,val))
#             if (i, j) not in indices and (j, i) not in indices :
#                 indices.append((i,j))
# print(f"resultat = {resultat}")
# print(f"indices = {indices}")

# # -----------------------------------------------------------------------------------------------------
# Exercice 9 : Anagrammes

# Vérifie si deux chaînes sont des anagrammes (mêmes lettres, ordre différent).

# chaine1 = "pythoncdd"
# chaine2 = "silent"
# chaine1 = list(chaine1)
# chaine2 = list(chaine2)
# if len(chaine1) != len(chaine2):
#     print("false len")
# chaine1.sort()
# chaine2.sort()

# if chaine1 == chaine2:
#     print("true")
# else:
#     print(False)

# # -----------------------------------------------------------------------------------------------------
# Exercice 10 : Premier caractère non répété

# Trouve le premier caractère qui n'apparaît qu'une seule fois dans une chaîne
# # Exemple
# chaine = "abacabad"
# # Résultat : 'c' (car a apparaît 3 fois, b 2 fois, c 1 fois)

# chaine = "aabbcc"
# # Résultat : None (tous sont répétés)

# chaine = "hello"
# # Résultat : 'h' (car h apparaît 1 fois, e 1 fois, mais h est le premier)
chaine = "abacabad"

# Étape 1 : compter les occurrences de chaque caractère
compteur = {}

# for c in chaine:  # ← on parcourt la chaîne directement
#     if c in compteur:
#         compteur[c] += 1
#     else:
#         compteur[c] = 1

# print(compteur)  # {'a': 4, 'b': 2, 'c': 1, 'd': 1}

# # Étape 2 : trouver le premier caractère avec un compteur = 1
# for c in chaine:  # ← on reparcourt la chaîne dans l'ordre
#     if compteur[c] == 1:
#         print(f"Le premier caractère non répété est : '{c}'")
#         break


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------