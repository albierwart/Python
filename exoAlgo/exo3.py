# Exercice 1 : Compression basique

# Écris une fonction qui prend une chaîne de caractères et retourne une version compressée selon la règle suivante :
#  chaque groupe de lettres identiques consécutives est remplacé par la lettre suivie du nombre d'occurrences.
#  Si une lettre apparaît une seule fois, on n'écrit pas le 1.

# Exemple : "AAABBC" → "A3B2C"

# Autre exemple : "ABBBCDDD" → "AB3CD3"

# texte = "AAABBC"

# def tri(texte):
#     reponse = []
#     for c in texte:
#         cpt = 0
#         for d in texte:
#             if d == c:
#                 cpt+=1
#         if cpt == 1:
#             rep = c
#         else:
#             rep = c + str(cpt)
#         if rep not in reponse:
#             reponse.append(rep)
#     repe = ""
#     for i in reponse:
#         repe = repe + str(i)
#     print(reponse)
#     print(repe)
# tri(texte)

# Exercice 2 : Sous-liste maximale croissante

# Écris une fonction qui prend une liste de nombres entiers et retourne la plus longue sous-liste strictement croissante 
# (éléments consécutifs dans la liste, pas une sous-séquence).

# Exemple : [1, 2, 3, 1, 2, 3, 4, 5, 0, 2, 3] → [1, 2, 3, 4, 5] (longueur 5)

# Autre exemple : [5, 4, 3, 2, 1] → [5] (longueur 1)

# liste = [1, 2, 3, 1, 2, 3, 4, 5, 0, 2, 3]

# def sousSequence(liste):
#     reponse = []
#     reponseFinal = []
#     for i in range(0, len(liste)):
#         if liste[i] < liste[i+1]:
#             reponse.append(liste[i])

# Bloc 1 : Les boucles simples (Exercices 1 à 5)
# Exercice 1
# Affiche les nombres de 1 à 20.

# for i in range(1,21):
#     print(i)

# Exercice 2
# Affiche tous les nombres pairs de 1 à 50.
# for i in range(1,51):
#     if i%2==0:
#         print(i)
# Exercice 3

# Demande un nombre à l'utilisateur et affiche sa table de multiplication de 1 à 10.
# nbr = int(input("donnez un nombre entre 1 et 20 "))
# for i in range (1,11):
#     print(f"{i} x {nbr} = {i*nbr}")

# Exercice 4

# Calcule la somme de tous les nombres de 1 à N (N est demandé à l'utilisateur).
# nbr = int(input("donnez un nombre "))
# reponse = 0
# for i in range(1, nbr+1):
#     reponse +=i
# print(reponse)

# Exercice 5

# Demande 5 nombres à l'utilisateur et affiche le plus grand.
# maxi = 0
# for i in range (1,6):
#     nbr = int(input("donnez un nombre "))
#     if nbr > maxi:
#       maxi = nbr
# print(maxi)


# Bloc 2 : Les chaînes de caractères (Exercices 6 à 10)
# Exercice 6

# Demande un mot à l'utilisateur et affiche le nombre de lettres qu'il contient.
# texte = input("donnez un mot ")
# print(f"ce mot contient {len(texte)} lettres")
# Exercice 7

# Demande un mot à l'utilisateur et affiche la première et la dernière lettre.
# texte = input("donnez un mot ")
# lettre1 = texte[0]
# lettreFin = texte[len(texte)-1]
# print(f"premiere lettre = {lettre1}  derniere lettre = {lettreFin}")

# Exercice 8

# Demande un mot à l'utilisateur et affiche son inverse (ex: "bonjour" → "ruojnob").
# texte = input("donnez un mot ")
# reponse = ""
# for i in range(len(texte)-1, -1, -1):
#     reponse = reponse+texte[i]
# print(reponse)
# Exercice 9

# Demande une phrase et compte combien de fois la lettre 'e' apparaît.
# texte = input("donnez une phrase")
# test = "e"
# cpt = 0
# for i in texte:
#     if i == test:
#         cpt += 1
# print(cpt)

# Exercice 10

# Demande un mot et affiche "C'est un palindrome" si le mot se lit pareil dans les deux sens (ex: "radar").
# texte = input("donnez un mot ")
# texte2 = ""

# for i in range(len(texte)-1, -1,-1):
#     texte2 = texte2 + texte[i]
# if texte == texte2:
#     print("ceci est un palindrome")
# else:
#     print("pas un palindrome")



# Bloc 3 : Les listes (Exercices 11 à 15)
# Exercice 11

# Crée une liste [5, 12, 8, 3, 9] et affiche chaque élément un par un.
# liste = [5, 12, 8, 3, 9]
# for n in liste:
#     print(n)
 
# Exercice 12

# Crée une liste de 5 nombres et affiche la somme de tous les éléments.
# liste = [5, 12, 8, 3, 9]
# reponse = 0
# for n in liste:
#     reponse+= n 
# print(reponse)
# Exercice 13

# Crée une liste [10, 20, 30, 40, 50] et remplace le troisième élément par 99. Affiche la nouvelle liste.

# liste =  [10, 20, 30, 40, 50]
# liste[2] = 99
# print(liste)
# Exercice 14

# Demande à l'utilisateur de remplir une liste de 5 nombres. Affiche le plus grand et le plus petit.
# import sys
# liste = []
# for i in range(0,5):
#     nbr = int(input("donnez un nombre "))
#     liste.append(nbr)
# maxi = 0
# min = sys.maxsize
# for n in liste:
#     if n < min:
#         min = n
#     if n > maxi:
#         maxi = n
# print(f"maxi = {maxi} min = {min}")
# Exercice 15

# Crée une liste contenant des nombres dont des doublons. Crée une nouvelle liste sans les doublons (en conservant l'ordre).

# liste = [1,2,2,5,5,6,8,9]
# listeSansDoublon = []
# for n in liste:
#     if n not in listeSansDoublon:
#         listeSansDoublon.append(n)
# print(listeSansDoublon)
# Bloc 4 : Les manipulations avancées (Exercices 16 à 20)
# Exercice 16

# Demande une liste de nombres à l'utilisateur (séparés par des espaces). Affiche la liste triée dans l'ordre croissant (sans utiliser sort).
# texte = input("donnez 5 nombres separer par un espace")
# nombres = texte.split()
# for i in nombres:
#     i = int(i)
# for i in nombres:
#     for j in nombres:
#         if i > j:
#             i,j = j,i

# print(nombres)


# Exercice 17

# Crée une liste [1, 2, 3, 4, 5]. Inverse l'ordre de la liste (sans utiliser reverse) et affiche le résultat.
# liste = [1, 2, 3, 4, 5]
# reverseListe = []
# for i in range(len(liste)-1, -1, -1):
#     reverseListe.append(liste[i])

# Exercice 18

# Demande une phrase. Crée un dictionnaire qui compte le nombre d'occurrences de chaque mot.

# texte = input("tapez une phrase ")
# mots = texte.split()
# dico = {}
# for i in mots:
#     cpt = 0
#     for j in mots:
#         if  i == j:
#             cpt+=1
#     if i not in dico:
#         dico[i] = cpt
# print(dico)


# Exercice 19

# Crée une liste de nombres. Écris une fonction qui prend cette liste et retourne une nouvelle liste contenant uniquement les nombres pairs.
# liste = [1, 2, 3, 4, 5]
# reponse = []
# for i in liste:
#     if i%2==0:
#         reponse.append(i)
# print(reponse)

# Exercice 20

# Crée une fonction qui prend une liste de mots et retourne la liste des mots qui commencent par une voyelle (a, e, i, o, u).
# texte = "Crée une fonction qui prend une liste de mots et retourne la liste des mots qui commencent par une voyelle"
# liste = texte.split()
# listeVoyelle = ["a","e","y","u", "i","o"]
# listeRep = []
# def motVoyelle(liste):
#     for i in liste:

#         if i[0] in listeVoyelle and i not in listeRep:
#             listeRep.append(i)
# motVoyelle(liste)
# print(listeRep)


# Exercice R1 : Compter à rebours (le plus simple)

# Écris une fonction récursive compte_a_rebours(n) qui affiche les nombres de n jusqu'à 0.

# Exemple : compte_a_rebours(5) affiche :
# text

# 5
# 4
# 3
# 2
# 1
# 0

# def compteRebour(n):
#     if n == 0:
#         print(0)
#         return 
#     print(n)
#     compteRebour(n -1)
# compteRebour(5)

# Exercice R2 : Compter de 0 à n

# Écris une fonction récursive compte_jusque(n) qui affiche les nombres de 0 jusqu'à n.

# Exemple : compte_jusque(5) affiche :
# text

# 0
# 1
# 2
# 3
# 4
# 5
# def compte_jusque(n):
#     if n == n:
#         return n
#     compte_jusque(n -1)
#     print(n)
# compte_jusque(5)