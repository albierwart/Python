import sys
import random


# # ---------------------------------------------------------------------------------------
# Exercice 1 : Liste des courses
# Crée une liste de courses vide. Demande à l'utilisateur d'ajouter des articles jusqu'à ce qu'il tape "fin".
#  Affiche la liste finale numérotée à partir de 1.

# courseList= list()

# while True:
#     reponse = input("ajoutez un article a votre liste de course ")
#     if reponse.lower() == "fin":
#         break

#     courseList.append(reponse)

# for i, value in enumerate(courseList):
#     print(f"{i+1}: {value}")

# # ---------------------------------------------------------------------------------------
# # Exercice 2 : Maximum et minimum
# Demande à l'utilisateur d'entrer des nombres séparés par des espaces, 
# puis affiche le plus grand et le plus petit sans utiliser min() et max().

# reponse = input("entrez des nombres separer par un espace ")
# listReponse = reponse.split()
# print(listReponse)
# for i, value in enumerate(listReponse):
#     listReponse[i] = int(listReponse[i])
# print(listReponse)
# min = sys.maxsize
# max = -sys.maxsize
# for n in listReponse:
#     if n > max:
#         max = n
#     if n < min:
#         min = n 
# print(f" min = {min} et max = {max}")
# # ---------------------------------------------------------------------------------------
# Exercice 3 : Suppression des doublons
# Demande une liste de nombres (séparés par des espaces) et
#  affiche la liste sans les doublons, en conservant l'ordre d'apparition.

# reponse = input("donnez une liste de nombre separe par des espaces ")
# listReponse = reponse.split()
# print(listReponse)
# for i, value in enumerate(listReponse):
#     listReponse[i] = int(listReponse[i])
# print(listReponse)
# listFinal = list()
# for n in listReponse:
#     if n not in listFinal:
#         listFinal.append(n)
# print(listFinal)


# ---------------------------------------------------------------------------------------

# # Exercice 4 : Compteur de lettres
# # Demande une phrase et affiche le nombre d'occurrences de chaque lettre 
# # (sans compter les espaces) dans un dictionnaire.

# texte = input("tapez une phrase ")
# sansEspaceTexte= texte.replace(" ","")
# listTexte = list(sansEspaceTexte)
# dicoTexte= {}
# for c in listTexte:
#     if c in dicoTexte:
#         dicoTexte[c] +=1
#     else:
#         dicoTexte[c] = 1
# print(dicoTexte)



# # ---------------------------------------------------------------------------------------
# Exercice 6 : Palindrome avec liste
# Demande une phrase et vérifie si c'est un palindrome (en ignorant les espaces et la casse).
# Utilise une liste pour inverser la chaîne.

# texte = input("donnez une prhase ")
# texteClean = texte.replace(" ", "").lower()
# texteList = list(texteClean)
# listLen = len(texteList)
# for i, value in enumerate(texteList):
#     if texteList[i] != texteList[listLen-1-i]:
#         print("ceci n est pas un palindrome")
#         break
# else:
#     print("c est un palindrome")

# # ---------------------------------------------------------------------------------------
# Exercice 7 : Matrice de multiplication
# Crée une matrice de multiplication 10x10 (table de Pythagore) et affiche-la proprement formatée.

# for ligne in range(1, 11):
#     for colonne in range(1, 11):
#         print(f"{ligne * colonne:>4}", end="")  # Aligné sur 4 caractères
#     print()
# ---------------------------------------------------------------------------------------
# Exercice 8 : Analyse de texte
# Demande un texte et affiche :

#     Le nombre total de mots

#     Le mot le plus long

#     La fréquence de chaque mot (dans un dictionnaire)

#     Les mots uniques triés alphabétiquement

# texte = input("encodez un texte a analyser ")
# nbrMot = texte.split()
# print(nbrMot)
# print(f"le nombre de mot est de {len(nbrMot)}")
# max = 0
# motMax = ""
# for m in nbrMot:
#     if len(m)> max:
#         max= len(m)
#         motMax=m
# print(f"le mot le plus long est {motMax}")
# dictMot = {}
# for v in nbrMot:
#     if v in dictMot:
#         dictMot[v] +=1
#     else:
#         dictMot[v] =1
# print(dictMot)
# dictMotTrie = dict(sorted(dictMot.items()))
# dictMotUnique=[]
# for cle,valeur in dictMotTrie.items():
#     if valeur==1:
#         dictMotUnique.append(cle)

# print(dictMotUnique)
# # ---------------------------------------------------------------------------------------
# Exercice 9 : Compteur de notes
# Demande des notes (entre 0 et 20) jusqu'à ce que l'utilisateur tape "fin". Affiche :

#     La moyenne

#     La note la plus haute et la plus basse

#     Combien de notes sont >= 10

#     La répartition dans un dictionnaire : {0-5: x, 5-10: x, 10-15: x, 15-20: x}
# ---------------------------------------------------------------------------------------
# listNote = []
# while True:
#     reponse = input("inserer  les notes avec un espace tapez fin pour terminer ")
#     if reponse == "fin":
#         break
#     else:
#         listNote.append(reponse)
# moyenne = 0
# for i,n in enumerate(listNote):
#     listNote[i] = int(listNote[i])
#     moyenne+=listNote[i]
# moyenne = moyenne/(len(listNote))
# print(moyenne)

# listNote.sort()
# print(f"la note la plus basse est {listNote[0]} et la plus haute est {listNote[len(listNote)-1]}")
# nbrPete = 0
# for i, values in enumerate(listNote):
#     if values == 11:
#         nbrPete=i
# print(f"nombre de notes sont >= 10 = {nbrPete}")
# dicNote = {"0-5":0, "6-10":0,"11-15":0,"16-20":0}
# for n in listNote:
#     if n < 6:
#         dicNote["0-5"] += 1
#     elif n < 11:
#         dicNote["6-10"] += 1 
#     elif n < 16:
#         dicNote["11-15"] +=1
#     else:
#         dicNote["16-20"] +=1

# print(dicNote)

# # ---------------------------------------------------------------------------------------
# Exercice 10 : Jeu du memory simplifié
# Crée une liste de 8 nombres (chaque nombre apparaît deux fois).
#  Mélange la liste (utilise random.shuffle()). 
# Le joueur doit trouver toutes les paires en choisissant deux indices à chaque tour. 
# Affiche la liste avec des "?" pour les indices non encore révélés.

# nbr = [10,10,20,20,30,30,40,40]
# random.shuffle(nbr)
# affichage = ["?"]*8
# print(affichage)
# while True:
#     reponse = input("entrez deux chiffres de 0 à 7 ")
#     reponse = reponse.split()
#     for i, value in enumerate(reponse):
#         reponse[i] = int(reponse[i])
#     indiceA = reponse[0]
#     indiceB = reponse[1]    
#     reponseA = nbr[indiceA]
#     reponseB = nbr[indiceB]
#     if reponseA == reponseB:
#         affichage[indiceA] = nbr[indiceA]
#         affichage[indiceB] = nbr[indiceB]
#     else:
#         print("valeur differente recommencez")
#     if "?" not in affichage:
#         print(affichage)
#         print("vous avez gagnez")
#         break

# # ---------------------------------------------------------------------------------------
# Exercice 11 : Transposition de matrice
# Demande une matrice sous forme de liste de listes 
# (ex: [[1,2,3],[4,5,6]]) et affiche sa transposée ([[1,4],[2,5],[3,6]]).

# # ---------------------------------------------------------------------------------------
# Exercice 12 : Dictionnaire inversé
# Crée un dictionnaire où plusieurs clés peuvent avoir la même valeur.
#  Inverse-le pour obtenir un dictionnaire où les valeurs deviennent des clés et les clés deviennent des listes de valeurs.

# Exemple : {"a": 1, "b": 2, "c": 1} → {1: ["a", "c"], 2: ["b"]}

dico = {"a" : 1}
print(dico)
for cle, value in dico.items():
    temp =dico[cle]
    # dico[i] = dico[value]
    dico[value] = temp
print(dico)



# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------