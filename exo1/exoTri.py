

# Tri par sélection
# 23/04/26
# Objectif : Trier la liste en plaçant le plus petit élément en première position,
#  puis le deuxième plus petit en deuxième position, etc.

# Règle : À chaque tour, cherche le minimum dans la partie non triée et
#  échange-le avec l'élément en position de début de cette partie.

# liste = [5, 2, 8, 1, 9]
# L = len(liste)
# print(liste)
# for i in range(0,L):
#     for j in range(i+1,L):
#         if liste[i]>liste[j]:
#             liste[i], liste[j]= liste[j], liste[i]
# print(liste)

# Tri par insertion

# Objectif : Trier la liste en prenant un par un les éléments de la partie non triée et
#  en les insérant à la bonne place dans la partie déjà triée.

# Règle : La partie gauche est toujours triée. On prend le premier élément de la partie droite,
#  on le sauvegarde, puis on décale vers la droite 
# tous les éléments de la partie gauche qui sont plus grands que lui, 
# enfin on l'insère à l'endroit libéré.

# liste = [5, 2, 8, 1, 9]
# L = len(liste)
# print(liste)
# temp = 0
# for i in range(0,L-1):
#     for j in range(i+1,-1,-1):
#         temp=liste[i]
#         if liste[i]<liste[j]:
#             liste[i] = liste[j]
# print(liste)

# Tri à bulles

# Objectif : Trier la liste en faisant "remonter" les grandes valeurs vers la fin
#  par des échanges successifs entre voisins.

# Règle : Parcourt la liste de gauche à droite, compare chaque paire d'éléments voisins. 
# S'ils sont dans le mauvais ordre, échange-les. 
# Recommence des passages jusqu'à ce qu'un passage entier n'ait provoqué aucun échange.

# liste = [5, 2, 8, 1, 9]
# L = len(liste)
# print(liste)
# for i in range(0,L):
#     for j in range(0, L):
#         if liste[i]<liste[j]:
#             liste[i], liste[j]= liste[j], liste[i]
# print(liste)

