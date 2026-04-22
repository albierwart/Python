import sys

# Exercice 1 : Liste des courses
# Crée une liste de courses vide. Demande à l'utilisateur d'ajouter des articles jusqu'à ce qu'il tape "fin".
# Affiche la liste finale numérotée à partir de 1.

# groceriesList = list()

# reponse = ""

# while(reponse != "fin"):
#     reponse = input("quel article ajouter a la liste? si plus tapez fin ")
#     if reponse == "fin":
#         break
#     groceriesList.append(reponse)

# for i, grocery in enumerate(groceriesList):
#     print(f"{i+1}: {grocery}")
# -------------------------------------------------------------------------------------------------
# Exercice 2 : Maximum et minimum
# Demande à l'utilisateur d'entrer des nombres séparés par des espaces, puis affiche le plus grand et 
# le plus petit sans utiliser min() et max().

# reponse = input("entre une serie de nombre separe par un espace ")
# print(reponse)
# resultat = reponse.split()

# for i in range(len(resultat)):
#     resultat[i] = int(resultat[i])

# min = sys.maxsize
# max = -sys.maxsize-1

# for num in resultat:
#     if num > max:
#         max = num
#     if num< min:
#         min = num
# print(f"valeur min: {min} et valeur max: {max}") 

# # -------------------------------------------------------------------------------------------------
# Exercice 3 : Suppression des doublons
# Demande une liste de nombres (séparés par des espaces) et affiche la liste sans les doublons,
# en conservant l'ordre d'apparition

# reponse = input("donnez une liste de nombre separe par un espace ")
# resultat = reponse.split()

# for i in range(len(resultat)):
#     resultat[i] = int(resultat[i])

# resultatFinal = [] 
# for valeur in resultat:
#     if valeur not in resultatFinal:
#         resultatFinal.append(valeur)
   
# for n in resultatFinal:
#     print(n, end=" ")
# -------------------------------------------------------------------------------------------------
# Exercice 4 : Compteur de lettres
# Demande une phrase et affiche le nombre d'occurrences de chaque lettre (sans compter les espaces) dans un dictionnaire.

# texte = input("entrez une phrase ")
# sansEspace = texte.replace(" ", "") 

# listLettre = list(sansEspace)
# dict = {}

# for letter in set(listLettre):
#     count = 0
#     for letters in listLettre:
#         if letter == letters:
#             count += 1
#     dict[letter] = count
# print(dict)

# -------------------------------------------------------------------------------------------------
# Exercice 5 : Fusion de listes
# Crée deux listes de même longueur, puis crée un dictionnaire où les éléments de la première liste
# sont les clés et ceux de la deuxième les valeurs.

# list1 = [1, 2, 3]
# list2 = ["pomme", "poire", "orange"]
# list3 = dict(zip(list1, list2))
# print(list3)

# # -------------------------------------------------------------------------------------------------
# Exercice 1 : Calculer la moyenne

# notes = [12, 15, 8, 19, 14]

# total=0
# nbrNote = len(notes)
# for n in notes:
#     total+=n
# print(f"la moyenne est de {total/nbrNote}")
# # # -------------------------------------------------------------------------------------------------
# # Exercice 2 : Compter les nombres pairs
# # Affiche "Il y a X nombres pairs"
# nombres = [3, 6, 9, 12, 15, 18]
# nbrPair = 0
# for n in nombres:
#     if n %2==0:
#         nbrPair+=1

# print(f"il y a {nbrPair} nombre pair dans la liste")

# # -------------------------------------------------------------------------------------------------
# Exercice 3 : Inverser la liste
# Inverse l'ordre : doit devenir [5, 4, 3, 2, 1]
# (sans utiliser reverse() ou [::-1])

# liste = [1, 2, 3, 4, 5]
# L = len(liste)

# for i in range(L//2):
#     temp = liste[i]
#     liste[i] = liste[L-1-i]
#     liste[L-1-i] = temp

# print(liste)
# # -------------------------------------------------------------------------------------------------
# Exercice 4 : Vérifier si la liste est triée
# Écris une fonction qui retourne True si la liste est triée croissante
# liste1 = [1, 3, 5, 7, 9]   # True
# liste2 = [2, 5, 3, 8, 4]   # False

# def estTrie(liste):
#     for i in range(len(liste)-1):
#         if liste[i] > liste[i+1]:
#             return False
#     return True

# print(estTrie(liste2))
# -------------------------------------------------------------------------------------------------
# Exercice 1 : Afficher toutes les paires d'éléments
# Affichage attendu :
# (1, 2)
# # (1, 3)
# # (2, 3)
# liste = [1, 2, 3]

# for i in range(len(liste)):
#     for j in range(i+1,len(liste)):
#         print((liste[i],liste[j]))
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------