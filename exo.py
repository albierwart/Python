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

# # -------------------------------------------------------------------------------
# Exercice 21 : Montée d'escaliers

# Combien de façons de monter N marches si on peut monter 1, 2 ou 3 marches à la fois ?
# def montee_escallier(n):
#     # Cas de base
#     if n == 0: 
#         return 1
#     if n == 1: 
#         return 1
#     if n == 2: 
#         return 2
#     if n == 3: 
#         return 4
    
#     # Tableau pour stocker les résultats (programmation dynamique)
#     # Taille n+1 car on veut l'index n
#     dp = [0] * (n + 1)
    
#     # Initialisation des cas de base
#     dp[0] = 1
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4
    
#     # Remplir le tableau de 4 à n
#     for i in range(4, n + 1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
#     # Retourner le résultat pour n marches
#     return dp[n]


# # Version optimisée (mémoire constante)
# def montee_escallier_optimise(n):
#     if n == 0: return 1
#     if n == 1: return 1
#     if n == 2: return 2
#     if n == 3: return 4
    
#     a, b, c = 1, 1, 2  # f(0)=1, f(1)=1, f(2)=2
#     resultat = 4        # f(3)=4
    
#     for i in range(4, n + 1):
#         resultat = c + b + a
#         a, b, c = b, c, resultat
    
#     return resultat


# # Version récursive avec mémoïsation
# def montee_escallier_recursif(n, memo={}):
#     if n in memo:
#         return memo[n]
    
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
    
#     memo[n] = montee_escallier_recursif(n-1, memo) + montee_escallier_recursif(n-2, memo) + montee_escallier_recursif(n-3, memo)
#     return memo[n]


# # Tests
# print("=== MONTÉE D'ESCALIER ===")
# print(f"Pour n = 1 : {montee_escallier(1)} façon")
# print(f"Pour n = 2 : {montee_escallier(2)} façons")
# print(f"Pour n = 3 : {montee_escallier(3)} façons")
# print(f"Pour n = 4 : {montee_escallier(4)} façons")
# print(f"Pour n = 5 : {montee_escallier(5)} façons")
# print(f"Pour n = 10 : {montee_escallier(10)} façons")

# print("\n=== AVEC LA VERSION OPTIMISÉE ===")
# for i in range(1, 11):
#     print(f"n = {i:2d} : {montee_escallier_optimise(i)} façons")

# print("\n=== AVEC LA VERSION RÉCURSIVE ===")
# for i in range(1, 11):
#     print(f"n = {i:2d} : {montee_escallier_recursif(i)} façons")

# # -------------------------------------------------------------------------------
# Exercice 24 : Plus grande sous-séquence croissante (LIS)

# Trouve la longueur de la plus longue sous-séquence strictement croissante.

# def plus_longue_sous_sequence_croissante(nums):
#     """
#     Retourne la longueur de la plus longue sous-séquence strictement croissante (LIS)
#     """
#     n = len(nums)
#     if n == 0:
#         return 0
    
#     # dp[i] = longueur de la LIS qui se termine à l'indice i
#     dp = [1] * n
    
#     # Remplir le tableau dp
#     for i in range(n):
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)
    
#     # Retourner la valeur maximale dans dp
#     return max(dp)


# # Version qui reconstruit UNE sous-séquence
# def plus_longue_sous_sequence_croissante_avec_sequence(nums):
#     """
#     Retourne la longueur ET une sous-séquence de longueur maximale
#     """
#     n = len(nums)
#     if n == 0:
#         return 0, []
    
#     dp = [1] * n
#     precedent = [-1] * n  # pour retracer la séquence
    
#     for i in range(n):
#         for j in range(i):
#             if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
#                 dp[i] = dp[j] + 1
#                 precedent[i] = j
    
#     # Trouver l'indice où la longueur est maximale
#     longueur_max = max(dp)
#     indice_max = dp.index(longueur_max)
    
#     # Reconstruire la séquence
#     sequence = []
#     i = indice_max
#     while i != -1:
#         sequence.append(nums[i])
#         i = precedent[i]
#     sequence.reverse()
    
#     return longueur_max, sequence


# # Tests
# print("=== PLUS GRANDE SOUS-SÉQUENCE CROISSANTE ===\n")

# # Test 1
# nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
# longueur, sequence = plus_longue_sous_sequence_croissante_avec_sequence(nums1)
# print(f"Entrée : {nums1}")
# print(f"Longueur maximale : {longueur}")
# print(f"Une sous-séquence : {sequence}")
# print()

# # Test 2
# nums2 = [3, 1, 4, 1, 5, 9, 2]
# longueur, sequence = plus_longue_sous_sequence_croissante_avec_sequence(nums2)
# print(f"Entrée : {nums2}")
# print(f"Longueur maximale : {longueur}")
# print(f"Une sous-séquence : {sequence}")
# print()

# # Test 3
# nums3 = [1, 2, 3, 4, 5]
# longueur, sequence = plus_longue_sous_sequence_croissante_avec_sequence(nums3)
# print(f"Entrée : {nums3}")
# print(f"Longueur maximale : {longueur}")
# print(f"Une sous-séquence : {sequence}")
# print()

# # Test 4
# nums4 = [5, 4, 3, 2, 1]
# longueur, sequence = plus_longue_sous_sequence_croissante_avec_sequence(nums4)
# print(f"Entrée : {nums4}")
# print(f"Longueur maximale : {longueur}")
# print(f"Une sous-séquence : {sequence}")
# print()

# # Version simple (juste la longueur)
# print("=== VERSION SIMPLE (JUSTE LA LONGUEUR) ===")
# print(f"[10, 9, 2, 5, 3, 7, 101, 18] → {plus_longue_sous_sequence_croissante(nums1)}")
# print(f"[3, 1, 4, 1, 5, 9, 2] → {plus_longue_sous_sequence_croissante(nums2)}")
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------