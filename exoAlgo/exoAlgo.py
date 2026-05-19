

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


# Exercice 8 : Tri à bulles (Bubble Sort)

# Implémente le tri à bulles. Ajoute une optimisation : arrête-toi si aucun échange n'a eu lieu.

# liste = [5,2,8,1,9]
# temp = 0
# counter = 0
# for j in range(len(liste) - 1):
#     for i in range(len(liste)):
#         if i == len(liste)-1:
#             continue
#         if liste[i] > liste[i+1]:
#             temp = liste[i]
#             liste[i] = liste[i+1]
#             liste[i+1]=temp
# print(liste)

# Exercice 9 : Tri par sélection (Selection Sort)
# Implémente le tri par sélection.
# import sys

# liste = [5,2,8,1,9]
# longueur = len(liste)

# indice = 0
# for i in range(longueur-1):
#     min =sys.maxsize
#     indice = 0
#     for j in range(i, longueur):
#         if liste[j] < min:
#             min = liste[j]
#             indice = j
#     temp = liste[i]
#     liste[i] = min
#     liste[indice]=temp
#     print(liste)

# print(liste)

# Exercice 10 : Tri par insertion (Insertion Sort)

# Implémente le tri par insertion.

# liste = [5, 2, 8, 1, 9]
# longueur = len(liste)

# # On commence à l'indice 1 car le premier élément (indice 0) est déjà "trié"
# for i in range(1, longueur):
    
#     # 1. On extrait l'élément à insérer
#     temp = liste[i]
    
#     # 2. On regarde les éléments à gauche (partie triée)
#     # On part de i-1 et on remonte vers la gauche
#     j = i - 1
    
#     # 3. On décale tous les éléments plus grands que temp vers la droite
#     while j >= 0 and liste[j] > temp:
#         liste[j + 1] = liste[j]  # décalage vers la droite
#         j = j - 1                 # on continue à gauche
    
#     # 4. On insère temp à sa place
#     liste[j + 1] = temp
    
#     # Affichage après chaque insertion (pour suivre l'évolution)
#     print(f"Après insertion de {temp} : {liste}")

# print("\nRésultat final :", liste)

# Exercice 11 : Tri fusion (Merge Sort)

# Implémente le tri fusion (récursif). C'est un classique d'entretien !



# Exercice 13 : Intersection de deux tableaux (le plus simple)

# Objectif : Trouver les éléments communs à deux listes, sans doublons.
# # Exemple
# liste1 = [1, 2, 3, 4, 5]
# liste2 = [4, 5, 6, 7, 8]

# # Résultat attendu
# [4, 5]

# liste1 = [1, 2, 3, 4, 5]
# liste2 = [4, 5, 6, 7, 8]

# liste3 = list(set(liste1) & set(liste2))
# print(liste3)
# liste4 = []
# for n in liste1:
#     if n in liste2 and n not in liste4:
#         liste4.append(n)
# print(liste4)

# Exercice 11 : Fusion de deux listes triées

# Objectif : Fusionner deux listes déjà triées en une seule liste triée.
# python

# # Exemple
# liste1 = [1, 3, 5, 7]
# liste2 = [2, 4, 6, 8]

# # Résultat attendu
# # [1, 2, 3, 4, 5, 6, 7, 8]
# liste1 = [1, 3, 5, 7]
# liste2 = [2, 4, 6, 8]
# liste3 = []

# i, j = 0, 0
# while i < len(liste1) and j < len(liste2):
#     if liste1[i] < liste2[j]:
#         liste3.append(liste1[i])
#         i+=1
#     else:
#         liste3.append(liste2[j])
#         j+=1
# while i < len(liste1):
#     liste3.append(liste1[i])
#     i+=1
# while j < len(liste2):
#     liste3.append(liste2[j])
#     j+=1
# print(liste3)



# Exercice 12 : Majorité (Boyer-Moore)

# Tu avais fait une version naïve (double boucle). Le but est de refaire avec l'algorithme de vote (un seul passage).
# python

# # Exemple
# liste = [3, 3, 4, 2, 3, 3, 3]

# # # Résultat attendu
# # 3
# liste = [2,3, 3, 4, 2, 3, 3, 3]

# compteur = 0
# candidat = 0

# for n in liste:
#     if compteur == 0:
#         candidat= n
#         compteur = 1
#     elif candidat == n:
#          compteur+=1
#     else:
#         compteur-=1

# print(candidat)

# occurence = 0
# for n in liste:
#     if n == candidat:
#         occurence+=1
# if occurence > len(liste)/2:
#     print(f"reponse = {candidat}")

# Exercice 15 : Fibonacci récursif

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1 :
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(9))

# Exercice 16 : Tours de Hanoï (récursif)

# def hanoi(n, depart, arrivee,intermediaire):
#     if n ==1:
#         print(f"deplacer disque 1 de {depart} vers {arrivee}")
#     else:
#         hanoi(n-1, depart, intermediaire, arrivee)
#         print(f"dplacer disque {n} de {depart} vers {arrivee}")
#         hanoi(n-1,intermediaire, arrivee,depart)
# hanoi(3, "A", "B", "C")

# def permutations(chaine):
#     # Cas de base
#     if len(chaine) <= 1:
#         return [chaine]
    
#     resultat = []
#     for i in range(len(chaine)):
#         caractere = chaine[i]
#         reste = chaine[:i] + chaine[i+1:]
        
#         for perm in permutations(reste):
#             resultat.append(caractere + perm)
    
#     return resultat
# print(permutations("abc"))

# Exercice 1 (Niveau 1)

# Compte les voyelles

# Compte le nombre de voyelles (a, e, i, o, u, y) dans une phrase saisie par l'utilisateur.
# python

# # Exemple
# Entrée : "Bonjour tout le monde"
# # Sortie : 8
# texte= "bonjour tout le monde"
# tabVoyelle = ["a", "e", "i", "o", "u", "y"]

# def nbrVoyelle (texte):
#     cpt = 0
#     for l in texte:
#         if l in tabVoyelle:
#             cpt+=1
#     print(cpt)

# nbrVoyelle(texte)
# ------------------------------------------------------------------------------------------------------------
# Exercice 2 (Niveau 2)

# Deux sommes

# Étant donné une liste de nombres et une cible, trouve toutes les paires (i, j) avec i < j dont la somme égale la cible.
# python

# # Exemple
# liste = [1, 2, 3, 4, 5, 6]
# cible = 7
# # Résultat attendu : [(1,6), (2,5), (3,4)] ou les indices
# liste = [1, 2, 3, 4, 5, 6]
# cible = 7
# listeResult=[]
# def deuxSomme(liste, cible):
#     for i in liste:
#         for j in range(i+1, len(liste)+1):
#             if i+j == cible:
#                 listeResult.append((i,j))
#     print(listeResult)
# deuxSomme(liste, cible)
# # ------------------------------------------------------------------------------------------------------------
# Exercice 3 (Niveau 1)

# Palindrome (version simple)

# Vérifie si un mot (pas une phrase) est un palindrome.
# python

# # Exemples
# "radar" → True
# "bonjour" → False
# texte = "bonjour"
# def estPalindrome(texte):
#     for i in range(0,len(texte)//2):
#         if texte[i] != texte[len(texte)-1-i]:
#             print("ce mot n est pas un palindrome")
#             break
#     else: print("True")

# estPalindrome(texte)

# ------------------------------------------------------------------------------------------------------------
# Exercice 4 (Niveau 3 - récursivité)

# Somme des chiffres (récursive)

# Écris une fonction récursive qui calcule la somme des chiffres d'un nombre.
# python

# # Exemple
# somme_chiffres(1234) → 10
# # Car 1+2+3+4 = 10
# nombre = 1234
# reponse = 0
# def sommeChiffre(nombre):
#     if(nombre == 0):
#         return 0
#     chiffre = nombre % 10
#     reste = nombre//10
    
#     return chiffre + sommeChiffre(reste)
# print(sommeChiffre(nombre))

# # ------------------------------------------------------------------------------------------------------------
# Exercice 5 (Niveau 2)

# Inverse un dictionnaire

# Prend un dictionnaire et inverse-le : les valeurs deviennent des clés, les clés deviennent des listes de valeurs.
# python

# # Exemple
# original = {"a": 1, "b": 2, "c": 1, "d": 3}
# # Résultat : {1: ["a", "c"], 2: ["b"], 3: ["d"]}

# original = {"a": 1, "b": 2, "c": 1, "d": 3}
# reponse = {}

# for cle, valeur in original.items():
#     if valeur not in reponse:
#         reponse[valeur] = []
#     reponse[valeur].append(cle)
# print(f" original = {original}")
# print(f"reponse = {reponse}")


# ------------------------------------------------------------------------------------------------------------
# Exercice 6 (Niveau 1)

# Nombre parfait

# Un nombre est parfait s'il est égal à la somme de ses diviseurs propres (excluant lui-même). Vérifie si un nombre est parfait.
# python

# # Exemple
# 6 → True (1+2+3 = 6)
# 28 → True (1+2+4+7+14 = 28)
# 12 → False
# nbr = 12
    
# def estNbrParfait(nbr):
#     listeDiviseur = []
#     for n in range(1 , nbr):
#         if nbr % n == 0:
#             listeDiviseur.append(n)
#     totChiffreListe = 0
#     for n in listeDiviseur:
#         totChiffreListe+= n
#     if totChiffreListe == nbr:
#         print("c est un nombre parfait")
#     else:
#         print("ce n est pas un nombre parfait")

# estNbrParfait(nbr)

# # ------------------------------------------------------------------------------------------------------------
# Exercice 7 (Niveau 2)

# Suppression des doublons

# Prend une liste et retourne une nouvelle liste sans doublons, en conservant l'ordre d'apparition.
# python

# # Exemple
# liste = [1, 3, 2, 3, 1, 4, 2, 5]
# # Résultat : [1, 3, 2, 4, 5]
# liste = [1, 3, 2, 3, 1, 4, 2, 5]
# def sansDoublon(liste):
#     listeReponse = []
#     for n in liste:
#         if n not in listeReponse:
#             listeReponse.append(n)
#     return print(listeReponse)
# sansDoublon(liste)
# # ------------------------------------------------------------------------------------------------------------
# Exercice 8 (Niveau 3 - récursivité)

# Puissance (récursive)

# Écris une fonction récursive qui calcule a^b (a puissance b) sans utiliser l'opérateur **.
# python

# # Exemple
# puissance(2, 5) → 32
# puissance(3, 3) → 27

# def fctPuissance(nbr, puissance):
#     if puissance == 1:
#         return nbr
#     return nbr * fctPuissance(nbr, puissance-1)
# print(fctPuissance(2,5))
# ------------------------------------------------------------------------------------------------------------
# Exercice 9 (Niveau 2)

# Occurrences d'un caractère

# Compte combien de fois chaque caractère apparaît dans une chaîne. Retourne un dictionnaire.
# python

# # Exemple
# Entrée : "bonjour"
# Sortie : {"b": 1, "o": 2, "n": 1, "j": 1, "u": 1, "r": 1}

# texte = "bonjouro"
# reponse = {}

# for c in texte:
#     if c not in reponse:
#         reponse[c] = 1
#     else:
#         cpt = reponse[c]
#         cpt+=1
#         reponse[c] = cpt
# print(reponse)

# ------------------------------------------------------------------------------------------------------------
# Exercice 10 (Niveau 1)

# PGCD (version itérative)

# Calcule le PGCD de deux nombres avec l'algorithme d'Euclide (version itérative, pas récursive).
# python

# # Exemple
# pgcd(48, 18) → 6
# pgcd(56, 42) → 14

# def pgcd(nbr , nbr2):
#     listeDivNbr = []
#     for n in range(1,nbr+1):
#         if nbr%n == 0:
#             listeDivNbr.append(n)
#     listeDivNbr2 = []
#     for chiffre in range(1,nbr2+1):
#         if nbr2%chiffre == 0:
#             listeDivNbr2.append(chiffre)
#     listDivCommunt = []
#     for n in listeDivNbr:
#         if n in listeDivNbr2:
#             listDivCommunt.append(n)
#     print(f"listeDivNbr : {listeDivNbr}")
#     print(f"listeDivNbr2 : {listeDivNbr2}")
#     print(f"listDivCommunt : {listDivCommunt}")

#     return print(listDivCommunt.pop())
# pgcd(48,18)

# # ------------------------------------------------------------------------------------------------------------
# Exercice 1

# Crée un dictionnaire vide. Ajoute-y trois paires : "nom" → "Alice", "age" → 25, "ville" → "Paris". Affiche le dictionnaire.
# Exercice 2

# À partir du dictionnaire de l'exercice 1, affiche la valeur associée à la clé "nom". Puis affiche la valeur associée à la clé "age".

# dico = {}
# dico ["nom"] = "alice"
# dico["age"] = 25
# dico["ville"] = "paris"

# print(dico["nom"])
# # print(dico["age"])

# Exercice 3
# Crée un dictionnaire des capitales : "France" → "Paris", "Allemagne" → "Berlin", "Italie" → "Rome". Demande un pays à l'utilisateur
#  et affiche sa capitale. Si le pays n'est pas dans le dictionnaire, affiche "Pays non trouvé".

# dico = {"france" : "paris",
#         "allemagne" : "berlin",
#         "italie" : "rome"
#         }
# demande = input("donnez un pays ")
# if demande not in dico:
#     print("pays pas dans dico")
# else:
#     print(dico[demande])

# Exercice 4

# Crée un dictionnaire contenant les notes de trois étudiants : 
# "Alice": 15, "Bob": 12, "Charlie": 18. Affiche le nom de l'étudiant qui a la meilleure note.

# dico = {"alice" : 15,
#         "bob" : 12,
#         "charlie" : 18}
# max = 0
# etudiant = ""
# for cle, valeur in dico.items():
#     if valeur > max:
#         max = valeur
#         etudiant = cle
# print(etudiant)


# ------------------------------------------------------------------------------------------------------------
# Bloc 2 : Parcours et manipulation (Exercices 5 à 8)
# Exercice 5

# Crée un dictionnaire {"pomme": 3, "banane": 5, "orange": 2}. Parcours le dictionnaire et affiche chaque paire sous la forme "fruit : quantité".
# dico = {"pomme": 3, "banane": 5, "orange": 2}

# for cle, valeur in dico.items():
#     print(f"{cle} : {valeur}")
# ------------------------------------------------------------------------------------------------------------

# Exercice 6
# Crée un dictionnaire avec 5 paires (clés et valeurs de ton choix). 
# Affiche toutes les clés sur une ligne.
#  Affiche toutes les valeurs sur une autre ligne.
# dico = {"pomme": 3, "banane": 5, "orange": 2, "noix": 10, "fraise": 15}
# for cle in dico.keys():
#     print(cle, end =" ")
# print()
# for valeur in dico.values():
#     print(valeur, end=" ")

# ------------------------------------------------------------------------------------------------------------
# Exercice 7
# Crée un dictionnaire {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}. 
# Crée une nouvelle liste qui contient uniquement les clés dont la valeur est supérieure à 3.
#  Affiche cette liste.
# dico = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# liste=[]
# for cle, valeur in dico.items():
#     if valeur > 3:
#         liste.append(cle)
# print(liste)

# ------------------------------------------------------------------------------------------------------------
# Exercice 8
# Crée un dictionnaire {"x": 10, "y": 20, "z": 30}.
#  Demande une clé à l'utilisateur. 
# Si la clé existe, affiche sa valeur. 
# Sinon, affiche "Clé inexistante" et ajoute cette clé avec la valeur 0.

# dico = {"x": 10, "y": 20, "z": 30}
# demande = input("donnez une lettre ")
# if demande not in dico:
#     dico[demande] = 0
# else:
#     print(f"la valeur de cette cle est {dico[demande]}")

# Bloc 3 : Comptage et occurrences (Exercices 9 à 12)

# ------------------------------------------------------------------------------------------------------------
# Exercice 9

# Demande une phrase à l'utilisateur. 
# Crée un dictionnaire qui compte le nombre de fois que chaque mot apparaît (majuscules/minuscules sont ignorées).
# Exemple : "Le chat et le chien" → {"le": 2, "chat": 1, "et": 1, "chien": 1}

# texte = input("donnez une phrase " )
# texte = texte.lower()
# texte= texte.split()
# dico = {}
# for mot in texte:
#     cpt = 0
#     for mot2 in texte:
#         if mot2 == mot:
#             cpt+=1
#     if mot not in dico:
#         dico[mot] = cpt
# print(dico)
# ------------------------------------------------------------------------------------------------------------
# Exercice 10

# Demande une phrase à l'utilisateur. 
# Crée un dictionnaire qui compte le nombre de fois que chaque lettre apparaît (ignore les espaces et la casse).
# Exemple : "bonjour" → {"b":1, "o":2, "n":1, "j":1, "u":1, "r":1}
# texte = input("donnez une phrase")
# texte = texte.lower()
# texte = texte.replace(" ", "")
# dico = {}
# for c in texte:
#     cpt = 0
#     for l in texte:
#         if c == l :
#             cpt+=1
#     if c not in dico:
#         dico[c] = cpt

# ------------------------------------------------------------------------------------------------------------
# Exercice 11

# Compte combien de fois chaque nombre apparaît dans la liste [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]. Affiche le dictionnaire résultat.
# # Exemple : {1:1, 2:2, 3:3, 4:4}
# pas fait car exactement le mm que le dix
# ------------------------------------------------------------------------------------------------------------
# Exercice 12

# Crée un dictionnaire à partir de deux listes : une liste de clés ["nom", "age", "ville"]
#  et une liste de valeurs ["Alice", 25, "Paris"]. Utilise zip().
# cle = ["nom", "age", "ville"]
# valeur = ["Alice", 25, "Paris"]
# personne = dict(zip(cle,valeur))


# Bloc 4 : Transformation et inversion (Exercices 13 à 16)

# ------------------------------------------------------------------------------------------------------------
# Exercice 13

# Crée un dictionnaire {"a": 1, "b": 2, "c": 3}. Crée un nouveau dictionnaire où les clés et les valeurs sont inversées : {1: "a", 2: "b", 3: "c"}.
# dico = {"a": 1, "b": 2, "c": 3}
# dico2 ={}
# for cle , valeur in dico.items():
#     dico2[valeur] = cle
# print(dico2)
# ------------------------------------------------------------------------------------------------------------
# Exercice 14

# Crée un dictionnaire {"a": 1, "b": 2, "c": 1, "d": 3}.
#  Inverse-le en regroupant les clés qui ont la même valeur dans une liste.
# Exemple : {1: ["a", "c"], 2: ["b"], 3: ["d"]}

# dico = {"a": 1, "b": 2, "c": 1, "d": 3}
# dico2 = {}
# for cle, valeur in dico.items():
#     if valeur not in dico2:
#         dico2[valeur] = list(cle)
#     else:
#         dico2[valeur].append(cle)
# print(dico2)

# ------------------------------------------------------------------------------------------------------------
# Exercice 15

# Crée un dictionnaire {"Alice": 15, "Bob": 12, "Charlie": 15, "Diana": 18}. 
# Inverser le dictionnaire pour que les notes deviennent des clés et les noms des listes de valeurs.
# Exemple : {15: ["Alice", "Charlie"], 12: ["Bob"], 18: ["Diana"]}
# dico = {"Alice": 15, "Bob": 12, "Charlie": 15, "Diana": 18}
# dico2 = {}
# for cle, valeur in dico.items():
#     if valeur not in dico2:
#         dico2[valeur] = list(cle)
#     else:
#         dico2[valeur].append(cle)
# print(dico2)

# ------------------------------------------------------------------------------------------------------------
# Exercice 16

# Crée un dictionnaire {"a": 5, "b": 2, "c": 8, "d": 1}. 
# Trouve la clé avec la plus grande valeur et celle avec la plus petite valeur. 
# Affiche les deux.
# dico = {"a": 5, "b": 2, "c": 8, "d": 1}
# min = 9999
# max = 0
# cleMin = ""
# cleMax= ""
# for cle, valeur in dico.items():
#     if valeur < min:
#         min = valeur
#         cleMin = cle
#     if valeur > max:
#         max = valeur
#         cleMax = cle
# print(f"cle max = {cleMax} et cle min = {cleMin}")

# Bloc 5 : Cas avancés (Exercices 17 à 20)

# ------------------------------------------------------------------------------------------------------------
# Exercice 17

# Crée un dictionnaire où les valeurs sont elles-mêmes des listes : {"A": [1, 2], "B": [3, 4], "C": [5, 6]}. 
# Calcule la somme des valeurs de chaque liste. Affiche la clé dont la somme est la plus grande.

# dico = {"A": [1, 2], "B": [3, 4], "C": [5, 6]}
# cleMax = 0
# for valeur in dico.values():
#     somme = 0
#     for i in valeur:
#         somme+= i
#     if somme> cleMax:
#         cleMax = somme
# print(cleMax)



# ------------------------------------------------------------------------------------------------------------
# Exercice 18

# Crée un dictionnaire {"produit1": 10, "produit2": 25, "produit3": 15, "produit4": 30}.
#  Multiplie toutes les valeurs par 1.20 (ajouter 20% de taxe). Affiche le dictionnaire modifié.

# dico = {"produit1": 10, "produit2": 25, "produit3": 15, "produit4": 30}
# for cle, valeur in dico.items():
#     valeur = valeur*1.20
#     dico[cle] = valeur
# print(dico)

# ------------------------------------------------------------------------------------------------------------
# Exercice 19

# Prends une liste de mots : ["pomme", "banane", "pomme", "orange", "banane", "banane"]. 
# Crée un dictionnaire qui compte les occurrences.
#  Ensuite, trouve le mot le plus fréquent.
# liste =  ["pomme", "banane", "pomme", "orange", "banane", "banane"]
# dico = {}
# for mot in liste:
#     if mot not in dico:
#         dico[mot] = 1
#     else:
#         dico[mot]+=1
# max = 0
# for cle, valeur in dico.items():
#     if valeur>max:
#         max = valeur
# for cle , valeur in dico.items():
#     if valeur == max:
#         print(f"reponse est {cle}")

# ------------------------------------------------------------------------------------------------------------
# Exercice 20

# Crée un dictionnaire à partir d'une phrase : les clés sont les mots, les valeurs sont la longueur de chaque mot.
# Exemple : "Le chat dort" → {"Le":2, "chat":4, "dort":4}

# texte = "Le chat dort"
# texte = texte.split()
# dico = {}
# for mot in texte:
#     dico[mot] = len(mot)
# print(dico)
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------