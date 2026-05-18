# Exercice 1 : Tri à bulles (Bubble Sort)
# Le principe

# On parcourt la liste plusieurs fois. À chaque passage, 
# on compare les éléments deux à deux et on les échange s'ils sont dans le mauvais ordre. 
# Les plus grands éléments "remontent" vers la fin comme des bulles.

# liste = [5, 3, 8, 1]
# for j in liste:
#     for i in range(0, len(liste)-1-j):
#         if liste[i] > liste[i+1]:
#             liste[i], liste[i+1] = liste[i+1], liste[i]
# print(liste)

# Exercice 2 : Tri par sélection (Selection Sort)

# Ce que doit faire l'algorithme :

# Tu parcours ta liste pour trouver le plus petit élément. Une fois trouvé, 
# tu le places à la première position (en l'échangeant avec l'élément qui s'y trouve). Ensuite, 
# tu cherches le deuxième plus petit élément et tu le places à la deuxième position, et ainsi de suite.

# À chaque étape, tu réduis la zone de recherche : le début de la liste devient de plus en plus trié, 
# et tu ne cherches que dans la partie non encore triée.

# liste = [64, 34, 25, 12, 22, 11, 90, 1]
# petit = 999
# indice = 999
# for i in range(len(liste)):
#     petit = 999
#     indice = 999
#     if liste[i] < petit:
#         petit = liste[i]
#         indice = i
#     for j in range(i+1, len(liste)):    
#         if liste[j]< petit:
#              petit=liste[j]
#              indice = j
#     temp = liste[i]
#     liste[i] = petit
#     liste[indice]= temp
# print(liste)


# Exercice 3 : Tri par insertion (Insertion Sort)

# Ce que doit faire l'algorithme :

# Imagine que tu as une main de cartes à trier. Tu prends les cartes une par une, 
# et tu les insères à la bonne place dans la partie déjà triée.

# Concrètement, tu commences avec le premier élément seul (il est déjà trié). 
# Puis tu prends le deuxième élément, tu le compares avec le premier,
#  et tu l'insères avant ou après selon sa valeur. Puis tu prends le troisième élément,
#  tu le compares avec les deux premiers, et tu l'insères à sa place, et ainsi de suite jusqu'à la fin.

# liste = [64, 34, 25, 12, 22, 11, 90, 1]
# listeTrie = []

# for i in range(len(liste)):
#     if listeTrie == []:
#         listeTrie.append(liste[i])
#     test = liste[i]

#     for j in range(len(listeTrie)):
#         if listeTrie[j] < test:
#             listeTrie.append(test)
#         else:
#             listeTrie.append(listeTrie[j])
#             listeTrie[j] = test
#             break

# print(listeTrie)

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# for i in range(1, len(liste)):
#     cle = liste[i]
#     j = i-1 

#     while j>=0 and liste[j] > cle:
#         liste[j+1] = liste[j]
#         j-=1
#     liste[j+1] = cle
# print(liste)
                         

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# for i in range(1, len(liste)):
#     cle = liste[i]
#     j = i-1

#     while j>=0 and liste[j]> cle:
#         liste[j+1] = liste[j]
#         j-=1
#     liste[j+1] = cle
# # print(liste)

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# for i in range(1, len(liste)):
#     cle = liste[i]
#     j = i-1

#     while j >= 0 and liste[j] > cle:
#         liste[j+1] = liste[j]
#         j-=1
#     liste[j+1] = cle
# print(liste)

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# for i in range(1, len(liste)):
#     cle = liste[i]
#     j = i-1
#     while j>=0 and liste[j] > cle:
#         liste[j+1] = liste[j]
#         j-=1
#     liste[j+1] = cle
# print(liste)

# Exercice 4 : Tri fusion (Merge Sort)

# Ce que doit faire l'algorithme :

# C'est un algorithme récursif (il s'appelle lui-même). Tu coupes ta liste en deux moitiés. 
# Tu tries chaque moitié séparément (en rappelant la même fonction).
#  Puis tu fusionnes les deux moitiés triées en une seule liste triée.

# Pour fusionner, tu compares les premiers éléments des deux moitiés, 
# tu prends le plus petit, et tu avances dans la moitié correspondante. 
# Tu continues jusqu'à avoir épuisé les deux moitiés.

# Le cas de base (pour arrêter la récursion) : si la liste n'a qu'un seul élément, 
# elle est déjà triée, tu la retournes telle quelle.

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# def triMerge(liste):
#     if len(liste)==1:
#         return liste
#     millieu = len(liste)//2
#     gauche = liste[:millieu]
#     droite = liste[millieu:]

#     gauche = triMerge(gauche)
#     droite = triMerge(droite)

#     return fusion(gauche, droite)

# def fusion(gauche, droite):
#     resultat = []
#     i = j = 0

#     while i < len(gauche) and j < len(droite):
#         if gauche[i] <= droite[j]:
#             resultat.append(gauche[i])
#             i += 1
#         else:
#             resultat.append(droite[j])
#             j += 1
    
#     while i < len(gauche):
#         resultat.append(gauche[i])
#         i+=1
#     while j < len(droite):
#         resultat.append(droite[j])
#         j+=1

#     return resultat

# liste = [64, 34, 25, 12, 22, 11, 90, 1]
# liste_triee = triMerge(liste)
# print(liste_triee) 

#  Tri rapide (Quick Sort)

# def triRapide(liste):
#     if len(liste)<=1:
#         return liste
    
#     pivot = liste[0]

#     gauche = []
#     millieu = []
#     droite = []

#     for n in liste:
#         if n < pivot:
#             gauche.append(n)
#         elif n == pivot:
#             millieu.append(n)
#         else:
#             droite.append(n)
#     return triRapide(gauche) + millieu + triRapide(droite)
# liste = [64, 34, 25, 12, 22, 11, 90, 1]
# liste_triee = triRapide(liste)
# print(liste_triee)

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# for i in range(1, len(liste)):
#     cle = liste[i]
#     j = i-1

#     while j >=0 and liste[j] > cle:
#         liste[j+1] = liste[j]
#         j-=1
#     liste[j+1] = cle
# print(liste)

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# for i in range(1, len(liste)):
#     cle = liste[i]
#     j = i-1

#     while j >=0 and liste[j] > cle:
#         liste[j+1] = liste[j]
#         j-=1
#     liste[j+1] = cle
# print(liste)

# liste = [64, 34, 25, 12, 22, 11, 90, 1]

# for i in range(1,len(liste)):
#     cle = liste[i]
#     j = i-1

#     while j>=0 and liste[j+1] > cle:
#         liste[j+1] = liste[j]
#         j-=1
#     liste[j+1] = cle
# print(liste)

liste = [64, 34, 25, 12, 22, 11, 90, 1]

for i in range(1, len(liste)):
    cle = liste[i]
    j = i-1

    while j >=0 and liste[j] > cle:
        liste[j+1] = liste[j]
        j-=1
    liste[j+1] = cle
print(liste)