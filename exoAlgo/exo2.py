# Exercice 11 : Fusion de deux listes triées

# Objectif : Fusionner deux listes déjà triées en une seule liste triée, sans utiliser sort().
# Exemple
# python

# # Entrée
# liste1 = [1, 3, 5, 7]
# liste2 = [2, 4, 6, 8]

# # Sortie attendue
# [1, 2, 3, 4, 5, 6, 7, 8]

# liste1 = [1,3,5,7]
# liste2 = [2,4,6,8]
# liste3 = []
          
# i, j = 0, 0

# while i < len(liste1) and j < len(liste2):
#     if liste1[i] < liste2[j]:
#         liste3.append(liste1[i])
#         i +=1
#     else:
#         liste3.append(liste2[j])
#         j +=1
# while i < len(liste1):
#     liste3.append(liste1[i])
#     i+=1
# while j < len(liste2):
#     liste3.append(liste2[j])
#     j+=1



# print(liste3)

# Exercice 13 : Intersection de deux tableaux (le plus simple)

# Objectif : Trouver les éléments communs aux deux listes, sans doublons.
# Exemple
# python

# # Entrée
# liste1 = [1, 2, 3, 4, 5]
# liste2 = [4, 5, 6, 7, 8]

# # Sortie attendue
# [4, 5]

# liste1 = [1, 2, 3, 4, 5]
# liste2 = [4, 5, 6, 7, 8]
# liste3 = []

# for i in liste1:
#     if i in liste2:
#         liste3.append(i)
# print(liste3)

# Exercice 12 : Majorité (Boyer-Moore) - le plus difficile

# Objectif : Trouver l'élément qui apparaît plus de la moitié du temps dans une liste.
# Exemple
# python

# # Entrée
# liste = [3, 3, 4, 2, 3, 3, 3]

# # Sortie attendue
# 3  # car 3 apparaît 5 fois sur 7 (> 3.5)

# liste = [3, 3, 4, 2, 3, 3, 3]
# liste2 = []

# for i in liste:
#     cpt = 0
#     if i in liste2:
#         continue
#     for j in liste:
#         if i == j:
#             cpt+=1
#     if cpt> (len(liste)/2):
#         liste2.append(i)
# print(liste2)

# def majorité_boyer_moore(liste):
#     # Phase 1 : trouver le candidat
#     candidat = None
#     compteur = 0
    
#     for element in liste:
#         if compteur == 0:
#             candidat = element
#             compteur = 1
#         elif element == candidat:
#             compteur += 1
#         else:
#             compteur -= 1
    
#     # Phase 2 : vérifier que le candidat est bien majoritaire
#     if compteur == 0:
#         return None  # Pas de majorité
    
#     occurrences = 0
#     for element in liste:
#         if element == candidat:
#             occurrences += 1
    
#     if occurrences > len(liste) / 2:
#         return candidat
#     else:
#         return None

# # Test
# liste = [3, 3, 4, 2, 3, 3, 3]
# # print(majorité_boyer_moore(liste))  # 3

# Exercice 14 : Factorielle récursive

# C'est le plus simple pour commencer la récursivité.

# def multi(n):
#     if n == 1:
#         return 1
#     return n*multi(n-1)

# # print(multi(5))

# Exercice 15 : Suite de Fibonacci récursive
# Rappel : Qu'est-ce que Fibonacci ?

# Chaque terme est la somme des deux précédents.

# listeFibo = []
# listeFibo.append(0) 
# listeFibo.append(1)
# nb = 5
# cpt=2
# while cpt<=nb:
#     listeFibo.append(listeFibo[cpt-1]+ listeFibo[cpt-2]) 
#     cpt+=1
# print(listeFibo) 


# def fibo(n):
#     if n == 0 :
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(5))

# Exercice 16 : Tours de Hanoï (récursif)
# Le problème

# Tu as 3 piquets : A (départ), B (auxiliaire), C (arrivée).

# Sur le piquet A, il y a n disques empilés du plus grand au plus petit.

# Règles :

#     Tu ne déplaces qu'un seul disque à la fois

#     Tu ne peux jamais placer un disque plus grand sur un disque plus petit

#     Tu dois déplacer tous les disques de A vers C

# La formule récursive

# Pour déplacer n disques de A vers C (avec B comme auxiliaire) :

#     Déplacer (n-1) disques de A vers B (avec C comme auxiliaire)

#     Déplacer le plus grand disque de A vers C

#     Déplacer (n-1) disques de B vers C (avec A comme auxiliaire)

# Cas de base : n = 1 → déplacer le disque de départ vers arrivée

A = [2,1]
B= []
C = []

aBouger = A.pop()
if not B:
    B.append(aBouger)
print(f"liste A: {A}")
print(f"liste B: {B}")
print(f"liste C: {C}")


