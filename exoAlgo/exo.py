import sys


# def test():
#     while reponse != "fin":


# Exercice 1 : Positif, négatif ou zéro
# Demande un nombre à l'utilisateur et affiche s'il est positif, négatif ou égal à zéro.

# reponse = int(input("donez un nombre "))

# def typeNumber(reponse):
#     if reponse == 0:
#         print(f"{reponse} est egal a zero")
#     elif reponse > 0:
#         print(f"{reponse} est un nombre positif")
#     else:
#         print("c'est un nombre negatif")

# typeNumber(reponse)

# # -------------------------------------------------------------------------------
# Exercice 2 : Voyelle ou consonne
# Demande une lettre à l'utilisateur et affiche si c'est une voyelle (a, e, i, o, u, y) ou une consonne.
#  Gère les majuscules et minuscules.


# reponse = input("donnez une lettre stp ")

# def typeLettre(reponse):
#     if reponse == "a" or reponse == "e" or reponse == "i" or reponse == "o" or reponse == "u" or reponse == "y":
#         print("vous avec encodez une voyelle")
#     else:
#         print("vous avez encode une consonne")

# # typeLettre(reponse)

# listeVoyelle = ["a", "e", "y","u", "i", "o"]

# def typeLettre2(reponse):
#     if reponse in listeVoyelle:
#         print("vous avec encodez une voyelle")
#     else:
#         print("vous avez encode une consonne")

# typeLettre2(reponse)
# # -------------------------------------------------------------------------------
# Exercice 3 : Le plus petit
# Demande trois nombres et affiche le plus petit.

# counter = 0
# listeNum = []
# while counter < 3:
#     listeNum.append(input("entre un nombre "))
#     counter += 1
# print(listeNum)

# for i, valeur in enumerate(listeNum):
#     listeNum[i] = int(listeNum[i])

# print(listeNum)

# lenTab = len(listeNum)
# for i in range(lenTab-1):
#     for j in range(lenTab-1):
#         if listeNum[j] > listeNum[j+1]:
#             listeNum[j], listeNum[j+1] = listeNum[j+1], listeNum[j]
# print(listeNum)

# ----------------------------------------------------------------

# Exercice 4 : Compteur à rebours avec message
# Demande un nombre de départ, puis affiche un compte à rebours. 
# À la fin, affiche "Bonne année !" si le nombre était 10, sinon "Décollage !".

# reponse = int(input("donnez un nombre "))
# counter = reponse
# while counter > 0:
#     print(counter)
#     counter-= 1
#     if counter == 0 and reponse == 10:
#         print("decollage")
#     if counter == 0 and reponse != 10:
#         print("bonne annee")

# # ---------------------------------------------------------------
# Exercice 5 : Table de multiplication inversée
# Demande un nombre et affiche sa table de multiplication, mais de 10 à 1 (ordre décroissant)

# nombre = int(input("donnez un nombre"))
# counter = 10
# while counter >=0:
#     print(f"{counter} x {nombre} = {counter* nombre}")
#     counter -= 1


# # -------------------------------------------------------------------------------
# Exercice 6 : Somme des pairs et des impairs
# Demande un nombre N. Calcule et affiche :

#     La somme des nombres pairs de 1 à N

#     La somme des nombres impairs de 1 à N


# number = int(input(" donnez un nombre "))
# numPair = 0
# numImpair = 0
# for i in range(1,number):
#     if i%2 == 0:
#         numPair+= i
#     else:
#         numImpair+=i
# print(f" la somme des impair de ce nombre est: {numImpair}")
# print(f" la somme des pair de ce nombre est: {numPair}")

# # -------------------------------------------------------------------------------
# Exercice 7 : Validation de mot de passe
# Demande un mot de passe à l'utilisateur. Il doit :

#     Faire au moins 8 caractères

#     Contenir au moins un chiffre

#     Contenir au moins une majuscule
#     Tant que le mot de passe n'est pas valide, redemander.
# def verifChiffre(test):
#      chifreList = ["1","2","3","4","5","6","7","8","9"]
#      charcListe = list(test)
#      for c in charcListe:
#           if c  in chifreList:
#                return True
#      return False
# def verifMaj(mot):
#      return mot != mot.lower() # 
#     #return mot.islower()
# condition = False
# while not condition:
#     reponse = input("donnez un mot de passe correcte. condition: + de  8 caractères, Contenir au moins un chiffre et Contenir au moins une majuscule ")
#     if len(reponse) >8 and verifChiffre(reponse) and verifMaj(reponse):
#          print("mot de passe accepte")
#          condition = True
#     else:
#          print("mauvais mot de passe ")


        
# verifChiffre("test")

# -------------------------------------------------------------------------------

# Exercice 1 : Affichage simple

# # Affiche les nombres de 1 à 20 en utilisant une boucle for.
# for i in range(20):
#     print(i+1, end=" ")
# # -------------------------------------------------------------------------------
# Exercice 2 : Nombres pairs

# Affiche tous les nombres pairs compris entre 1 et 50.

# for i in range(51):
#     if i%2 == 0:
#         print(i, end=" ")

# # -------------------------------------------------------------------------------
# Exercice 3 : Compte à rebours

# # Affiche un compte à rebours de 10 à 1, puis affiche "Décollage !".
# decompte = 10
# for i in range(decompte+1):
#    if decompte>0:
#       print(decompte, end=" ")
#    if decompte == 0:
#       print("decolage")
#    decompte -=1

# # -------------------------------------------------------------------------------

# # Exercice 6 : Pair ou impair

# # Parcours une liste de nombres et affiche pour chacun s'il est pair ou impair.

# valeurs = [45, 78, 12, 89, 34, 67, 23, 90, 56]

# for n in valeurs:
#    if n%2==0:
#       print("pair")
#    else:
#       print("impair")

# # -------------------------------------------------------------------------------
# Exercice 9 : Inversion de liste

# Inverse l'ordre d'une liste sans utiliser reverse() ou [::-1].

# ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# longueur = len(ma_liste)
# temp = 0
# for i, valeur in enumerate(ma_liste):
#    temp= ma_liste[i]
#    ma_liste[i]= ma_liste[longueur-1 -i]
#    ma_liste[longueur-1 -i] = temp
#    if i > longueur/2:
#       break
# print(ma_liste)
# # # -------------------------------------------------------------------------------
# Exercice 10 : FizzBuzz

# Affiche les nombres de 1 à 100 avec les règles suivantes :

#     Si le nombre est multiple de 3, affiche "Fizz"

#     Si le nombre est multiple de 5, affiche "Buzz"

#     Si le nombre est multiple de 3 ET de 5, affiche "FizzBuzz"

#     Sinon, affiche le nombre

# for n in range(100):
#     if n%15==0:
#         print("fizzbuzz", end=" ")
#     elif n%3==0:
#         print("fizz", end=" ")
#     elif n%5==0:
#         print("buzz", end=" ")
#     else:
#         print(n, end=" ")


# # -------------------------------------------------------------------------------
# Exercice 11 : Suppression des doublons

# # À partir d'une liste contenant des doublons, crée une nouvelle liste sans doublons tout en conservant l'ordre d'apparition.

# avec_doublons = [1, 2, 3, 2, 1, 4, 5, 3, 6, 4, 7, 8, 5]

# newListe = []

# for i in avec_doublons:
#     if i not in newListe:
#         newListe.append(i)
# print(newListe, end=" ")

# # # -------------------------------------------------------------------------------
# Exercice 14 : Matrice et somme des diagonales

# Pour une matrice carrée (liste de listes), calcule la somme de la diagonale principale et de la diagonale secondaire.
# python


# Diagonale principale : 1 + 5 + 9 = 15
# Diagonale secondaire : 3 + 5 + 7 = 15

# matrice = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# diagoPincipale = 0
# diagoSec = 0
# for i, valeur in enumerate(matrice):
#     compteur = 0
#     while compteur<1:
#         diagoPincipale+=valeur[i]
#         compteur+=1

# for i, valeur in enumerate(matrice):
#     compteur = 0 
#     while compteur<1:
#         diagoSec+= valeur[len(matrice)-1-i]
#         compteur+=1
#         print(valeur[len(matrice)-1-i])

# print(f"diago principale = {diagoPincipale}" )
# print(f"diago secondaire = {diagoSec} " )
# # -------------------------------------------------------------------------------
# Exercice 15 : Nombre premier

# Demande un nombre à l'utilisateur et affiche s'il est premier ou non.

# nombre = int(input("donnez un nombre "))

# for i in range(2, nombre):
#     if nombre % i ==0:
#         print("ce n est pas un nombre premier")
#         break
# else:
#     print("c est un nombre premier")


# # -------------------------------------------------------------------------------
# # FACTORIELLE RÉCURSIVE
# pour n donner n*n-1 jusqua 1

# n=5
# resultat = 0
# def facto(n):
#     if n < 1:
#         return 1    
#     return n*facto(n-1)
# print(facto(n))

# # -------------------------------------------------------------------------------
# Exercice 15 : Suite de Fibonacci

# n=9
# liste = []
# liste.append(0) 
# liste.append(1)
# counter = 2
# while counter<n:
#     liste.append(liste[counter-1]+ liste[counter-2])
#     counter+=1
# print(liste)
# n=9
# valMoinsDeux=0
# valMoinsUn=1
# print(f"{valMoinsDeux}, {valMoinsUn}, ", end="")
# counter=2
# while counter<n:
#     fibo = valMoinsDeux+valMoinsUn
#     print(f"{fibo}, ", end="")
#     valMoinsDeux = valMoinsUn
#     valMoinsUn = fibo
#     counter+=1

# -------------------------------------------------------------------------------
# Exercice 15 : Suite de Fibonacci recursive
# n=9
# counter = 0
# def fibo(n1,n2, counter,n):
#     counter+=1
#     if n == counter:
#         return n1
#     return fibo(n2, n1+n2, counter,n)
# print(fibo(0,1,counter,n))


# -------------------------------------------------------------------------------
# # Exercice 17 : Puissance rapide

# # Calcule x^n en O(log n) avec la méthode :

# #     Si n est pair : x^n = (x^(n/2))²

# #     Si n est impair : x^n = x * x^(n-1)

# n = 2
# puissance = 10

# def puissance(n, puissance):


# # # -------------------------------------------------------------------------------
# Exercice 19 : Permutations d'une chaîne

# Génère toutes les permutations possibles d'une chaîne.

# #    permutations("abc") → ["abc", "acb", "bac", "bca", "cab", "cba"] 
# def permutations_detail(chaine, etape=0):
#     """
#     Version avec affichage pour comprendre le processus
#     """
#     print(f"{'  ' * etape}Permutations de '{chaine}'")
    
#     if len(chaine) <= 1:
#         print(f"{'  ' * etape}  Retourne : [{chaine}]")
#         return [chaine]
    
#     resultat = []
    
#     for i in range(len(chaine)):
#         caractere = chaine[i]
#         reste = chaine[:i] + chaine[i+1:]
#         print(f"{'  ' * etape}  Caractère '{caractere}', reste '{reste}'")
        
#         for perm in permutations_detail(reste, etape + 1):
#             resultat.append(caractere + perm)
    
#     print(f"{'  ' * etape}  Retourne : {resultat}")
#     return resultat


# print("=== DÉTAIL DU PROCESSUS ===")
# print("\nPermutations de 'abc' :")
# resultat = permutations_detail("abc")
# print(f"\nRésultat final : {resultat}")

# -------------------------------------------------------------------------------

# Exercice 1 : Multiplication par addition

# Écris un programme qui multiplie deux nombres entiers positifs sans utiliser l'opérateur * (ni *=). 
# Tu dois utiliser une boucle qui additionne le premier nombre à lui-même
# autant de fois que la valeur du deuxième nombre.

# def miltplication(nbr, multiplacateur):
#     reponse = 0
#     for n in range(multiplacateur):
#         reponse += nbr
#     return reponse
# print(miltplication(2,5))


# -------------------------------------------------------------------------------
# Exercice 2 : Inversion de l'ordre des mots

# Demande à l'utilisateur de saisir une phrase (plusieurs mots séparés par des espaces). '
# 'Affiche la même phrase mais dans l'ordre inverse des mots.

# Exemple : "bonjour tout le monde" → "monde le tout bonjour"

# texte = "bonjour tout le monde"

# for mot in texte:
#     print(mot)
# phrase = "Bonjour tout le monde"
# texte = ""
# mots = phrase.split()  # coupe aux espaces
# print(mots)  # ['Bonjour', 'tout', 'le', 'monde']

# # Parcourir tous les mots
# i = len(mots)-1
# while i >=0:
#     texte = texte + mots[i] + " " 
#     i-=1
# print(phrase)
# print(texte)

# -------------------------------------------------------------------------------
# Exercice 3 : Triangle d'étoiles

# Demande un nombre entier N à l'utilisateur. Affiche un triangle rectangle isocèle d'étoiles (*) de hauteur N,
# avec l'angle droit en bas à gauche.

# def affTriange(nbr):
#     for i in range(1,nbr+1):
#         print("*" * i)

# affTriange(5)

# -------------------------------------------------------------------------------
# Exercice 4 : Somme des entiers pairs compris entre deux bornes

# Demande deux nombres entiers A et B à l'utilisateur (sans hypothèse sur l'ordre). 
# Calcule et affiche la somme des entiers pairs compris entre ces deux bornes, bornes incluses.

# Exemple : A = 3, B = 10 → les entiers pairs sont 4, 6, 8, 10 → somme = 28
# -------------------------------------------------------------------------------
# def sommePair(nbr1, nbr2):
#     reponse = 0
#     if nbr2<nbr1:
#         temp = nbr2
#         nbr2 = nbr1
#         nbr1 = temp
#     for n in range(nbr1, nbr2+1):
#         if n%2==0:
#             reponse += n
#     return print(reponse)
# sommePair(3,10)


# -------------------------------------------------------------------------------
# Exercice 5 : Devinette

# Le programme choisit un nombre aléatoire entre 1 et 50. 
# Le joueur doit deviner ce nombre. À chaque essai, le programme lui dit si le nombre est "plus grand", "plus petit", ou "bravo !"
# s'il a trouvé. Le programme compte et affiche le nombre d'essais au moment de la victoir
# import random
# aTrouver = random.randint(1,50)
# print(aTrouver)
# reponse = int(input("donner un nombre entre 1 et 50 "))
# essai = 0
# while reponse != aTrouver:
#     if aTrouver < reponse:
#         print("les chiffre a trouver est plus petit")
#         essai+=1
#         reponse = int(input(f"donner un nombre entre 1 et {reponse} "))
#     elif aTrouver > reponse:
#         print("le chiffre a trouver est plus grand")
#         essai+=1
#         reponse = int(input(f"donner un nombre entre {reponse} et 50 "))
# else:
#     essai+=1
#     print(f" bravo tu as trouve en {essai} tentative")



# # -------------------------------------------------------------------------------
# Exercice 1 : Compression basique

# Écris une fonction qui prend une chaîne de caractères et retourne une version compressée selon la règle suivante : 
# chaque groupe de lettres identiques consécutives est remplacé par la lettre suivie du nombre d'occurrences.
#  Si une lettre apparaît une seule fois, on n'écrit pas le 1.

# Exemple : "AAABBC" → "A3B2C"

# Autre exemple : "ABBBCDDD" → "AB3CD3"

# def transform(texte):
#     reponse = ""
#     for i,c in enumerate(texte):
#         cpt = 1
#         if texte[i+1] != c:
#             reponse += f"{c}" 
#     print(reponse)


# transform("AAABBC")
# -------------------------------------------------------------------------------
# Exercice 2 : Sous-liste maximale croissante

# Écris une fonction qui prend une liste de nombres entiers et retourne la plus longue sous-liste strictement croissante 
# (éléments consécutifs dans la liste, pas une sous-séquence).

# Exemple : [1, 2, 3, 1, 2, 3, 4, 5, 0, 2, 3] → [1, 2, 3, 4, 5] (longueur 5)

# Autre exemple : [5, 4, 3, 2, 1] → [5] (longueur 1)

# liste = [1, 2, 3, 1, 2, 3, 4, 5, 0, 2, 3]

# def fonct(liste):
#     reponse = []
#     reponseFinal = []
#     for n in range(0, len(liste)-1):
#         if liste[n] < liste[n+1]:
#             reponse.append(liste[n])
#         if len(reponse) > len(reponseFinal):
#             reponseFinal = reponse.copy()
#             reponse = []

#     print(reponseFinal)
# fonct(liste)

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------