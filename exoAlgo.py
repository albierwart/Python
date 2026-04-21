

# Exercice 1 : Inversion de chiffres

# Écris un algorithme qui inverse les chiffres d'un nombre entier.

# number = 12345
# inverse = 0
# print(inverse)
# while number>0:
#     reste = number%10
#     number = number//10
#     inverse = inverse*10+reste
#     print(f"number : {number}")
#     print(f"reste : {reste}")
#     print(f"inverse : {inverse}")

#     print("-"*20)
# print(inverse)

# Exercice 2 : Palindrome

# Vérifie si un mot ou une phrase est un palindrome (se lit pareil dans les deux sens).

# texte = "radar"
# texteSansespace= texte.replace(" ","").lower()
# taille = len(texteSansespace)
# listeTexte = str(texteSansespace)
# for i in range(taille//2):
#     if listeTexte[i] != listeTexte[taille-1-i]:
#         print("ce n est pas un palindrome")
#         break
# else:
#     print("c est un palindrome")

# Exercice 3 : Nombre d'occurrences

# Compte combien de fois une lettre apparaît dans une phrase sans utiliser la méthode count()

# texte = "bonjour"

# recherche = input(f"quelle lettre rechechez vous dans:{texte} ")
# counter = 0
# for c in texte:
#     if c == recherche:
#         counter+= 1
# print(counter)

# Exercice 5 : Nombre premier

# Détermine si un nombre est premier.

# nombre = 15
# for n in range(2,nombre):
#     if nombre % n == 0:
#         print("ce n est pas un nombre premier")
#         break
# else:
#     print("c est un nombre premier")

# Exercice 6 : PGCD (Plus Grand Commun Diviseur)

# Calcule le PGCD de deux nombres (algorithme d'Euclide).

# nombre1 = 18
# nombre2 = 24

# listeDiviseurNombre1 = []
# listeDiviseurNombre2 = []

# for n in range(1,nombre1+1):
#     if nombre1 %n ==0:
#         listeDiviseurNombre1.append(n)
# for n in range(1,nombre2+1):
#     if nombre2 %n ==0:
#         listeDiviseurNombre2.append(n)
# listeDiviseurCommun=[]
# for n in listeDiviseurNombre1:
#     if n in listeDiviseurNombre2:
#         listeDiviseurCommun.append(n)
# print(listeDiviseurCommun[-1])

# Exercice 7 : Suppression des doublons

# Prend une liste et retourne une nouvelle liste sans doublons, en conservant l'ordre

# listNbr = [1,2,3,5,6,3,5,6,9]
# listFinal = []
# for n in listNbr:
#     if n not in listFinal:
#         listFinal.append(n)
# print(listNbr)
# print(listFinal)

# Exercice 8 : Somme de deux nombres dans une liste

# Étant donné une liste de nombres et une cible, trouve deux nombres dont la somme égale la cible.

# liste = [2,7,11,15]
# cible = 9

# for n1 in liste:
#     for n2 in liste:
#         if n1 + n2 == cible:
#             print(f"{cible} = {n1} + {n2} ")
#             break
liste = [2, 7, 11, 15]
cible = 9

# # Exercice 9 : Anagrammes

# # Vérifie si deux chaînes sont des anagrammes (mêmes lettres, ordre différent)

# texte1 = "listen"
# texte2 = "silent"

# texte1 = "".join(c for c in texte1 if c.isalpha())
# print(texte1)

# Exercice 10 : Premier caractère non répété

# Trouve le premier caractère qui n'apparaît qu'une seule fois dans une chaîne

# texte = "abacabad"
# dicoC = {}
# for c in texte:
#     if c in dicoC:
#         dicoC[c] += 1
#     else:
#         dicoC[c] = 1
# for i,v in dicoC.items():
#     if v == 1:
#         print(i) 
# #         break
# Exercice 11 : Fusion de deux listes triées

# Fusionne deux listes triées en une seule liste triée (sans utiliser sort()).

# liste1 = [1,3,5]
# liste2 = [2,4,6]
# listeFinal = []

# i,j = 0,0

# while i<len(liste1) and j<len(liste2):
#     if liste1[i] < liste2[j]:
#         listeFinal.append(liste1[i])
#         i+=1
#     else:
#         listeFinal.append(liste2[j])
#         j+=1
# while i < len(liste1):
#     listeFinal.append(liste1[i])
#     i+=1
# while j <len(liste2):
#     listeFinal.append(liste2[j])
#     j+=1
# print(listeFinal)

# Exercice 12 : Majorité (Algorithme de Boyer-Moore)

# Trouve l'élément qui apparaît plus de la moitié du temps dans une liste.

# def boyer_moore_pas_a_pas(texte, motif):
#     """Version pédagogique qui affiche chaque étape"""
#     N = len(texte)
#     M = len(motif)
    
#     if M == 0 or M > N:
#         return []
    
#     # Table du mauvais caractère
#     table = {}
#     for i in range(M):
#         table[motif[i]] = M - 1 - i
    
#     print(f"Table du mauvais caractère pour '{motif}':")
#     for lettre, decalage in table.items():
#         print(f"  '{lettre}' → décalage {decalage}")
#     print(f"  Autres lettres → décalage {M}")
#     print()
    
#     positions = []
#     position = 0
    
#     while position <= N - M:
#         print(f"\n--- Alignement à la position {position} ---")
#         print(f"Texte : {texte}")
#         print(f"Motif : {' ' * position}{motif}")
        
#         j = M - 1
#         while j >= 0 and motif[j] == texte[position + j]:
#             j -= 1
        
#         if j < 0:
#             print(f"✓ TROUVÉ à la position {position} !")
#             positions.append(position)
#             position += 1
#         else:
#             print(f"✗ Différence à l'indice {j}: motif[{j}]='{motif[j]}' vs texte[{position + j}]='{texte[position + j]}'")
#             lettre_texte = texte[position + j]
            
#             if lettre_texte in table:
#                 decalage = table[lettre_texte]
#                 print(f"  '{lettre_texte}' trouvé dans le motif → décalage = {decalage}")
#             else:
#                 decalage = M
#                 print(f"  '{lettre_texte}' non trouvé dans le motif → décalage = {decalage}")
            
#             avance = j - decalage + 1
#             if avance <= 0:
#                 avance = 1
            
#             print(f"  Avance de {avance} case(s)")
#             position += avance
    
#     return positions


# # Tester la version pédagogique
# print("\n" + "=" * 60)
# print("VERSION PÉDAGOGIQUE AVEC AFFICHAGE")
# print("=" * 60)

# texte_test = "abcxabd"
# motif_test = "abd"
# print(f"\nRecherche de '{motif_test}' dans '{texte_test}'\n")
# resultat = boyer_moore_pas_a_pas(texte_test, motif_test)
# print(f"\nRésultat final : motif trouvé aux positions {resultat}")


# Exercice 13 : Intersection de deux tableaux

# Trouve les éléments communs à deux tableaux (sans doublons)

# liste1 = [1, 2, 3, 4, 5, 6]
# liste2 = [4, 5, 6, 7, 8, 9]
# listeFin = []

# for n in liste1:
#     if n in liste2 and n not in listeFin:
#         listeFin.append(n)
# print(listeFin)
        
# Exercice 1 : Recherche linéaire

# # Écris une fonction qui cherche un élément dans une liste et retourne son index (ou -1 si non trouvé)

# liste = [1,2,3,4,5,6,7,8,9]

# def indice(cible):
#     for i in range(len(liste)):
#         if cible == liste[i]:
#              print(i)
#     else:
#           print(f"-1")
# indice(9)

# Exercice 2 : Recherche dichotomique (binaire)

# Implémente la recherche dichotomique sur une liste triée. Complexité : O(log n)

# liste = [1,2,3,4,5,6,7,8,9]

# gauche = 0
# droite = len(liste)-1
# recherche = True
# cible = 7

# while gauche<=droite:
#     millieu = (droite+gauche)//2
#     if cible == liste[millieu]:
#         print("trouve")
#         break
    
#     if liste[millieu] < cible:
#         gauche = millieu+1
#     else:
#         droite = millieu -1
# import sys
# # Exercice 3 : Trouver le minimum et le maximum

# # Trouve le min et le max d'une liste en une seule passe (pas deux parcours séparés)


# def min_max(liste):
#     min = sys.maxsize
#     max = -sys.maxsize
#     for n in liste:
#         if n < min:
#             min = n
#         elif n>max:
#             max = n
#     print(f"min:{min}  max:{max}")

# min_max([3, 7, 1, 9, 2])

# Exercice 5 : Somme des éléments

# Calcule la somme des éléments d'une liste (récursif et itératif).

# liste = [1,2,3,4,5]

# def somme(liste):
#     total = 0
#     for n in liste:
#         total+= n    
#     return total
# print(somme(liste))

# Exercice 6 : Inversion de liste

# Inverse une liste sans utiliser [::-1] ou reverse().

# def inverser(liste):
#     temp = 0
#     for i in range(len(liste)//2):
#         temp= liste[i]
#         liste[i] = liste[len(liste)-1-i]
#         liste[len(liste)-1-i] = temp
# liste = [1, 2, 3, 4, 5]
# inverser(liste)
# print(liste)

# Exercice 7 : Palindrome (version nombre)

# Vérifie si un nombre est un palindrome sans le convertir en chaîne.

# def est_palindrome(nombre):
#     # Les nombres négatifs ne sont pas des palindromes (le signe - pose problème)
#     if nombre < 0:
#         return False
    
#     original = nombre
#     inverse = 0
    
#     while nombre > 0:
#         dernier_chiffre = nombre % 10
#         inverse = inverse * 10 + dernier_chiffre
#         nombre = nombre // 10
    
#     return original == inverse

# # Tests
# print(est_palindrome(12321))  # True
# print(est_palindrome(12345))  # False
# print(est_palindrome(1221))   # True
# print(est_palindrome(7))      # True (un seul chiffre)
# print(est_palindrome(-121))   # False (négatif)