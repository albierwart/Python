
# 1 Trouver les indices de deux nombres dans une liste dont la somme est égale à une cible.

# nums = [3, 2, 4, 7, 11, 15]
# target = 6
# reponse= []
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i == j:
#             continue
#         if nums[i] + nums[j] == target and (j,i) not in reponse:
#             reponse.append((i,j))
# print(reponse)

# nums = [3, 2, 4, 7, 11, 15]
# target = 6

# def two_sum(nums, target):
#     memo = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in memo:
#             return [memo[complement], i]
        
#         memo[num] = i

# print(two_sum(nums, target))
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# Trouver le plus grand nombre dans une liste
# Contraintes
# pas de max()
# une seule boucle
# pas de tri
# import sys
# nums = [3, 7, 2, 9, 4, 1]
# max = -sys.maxsize
# for num in nums:
#     if num> max:
#         max = num
# print(max)

# nums = [3, 7, 2, 9, 4, 1]
# max = nums[0]
# for num in nums:
#     if num > max:
#         max = num
# print(max)

# # -----------------------------------------------------------------------------------------------------------
# Trouver le deuxième plus grand nombre
# Contraintes
# pas de tri
# une seule boucle
# pas de max()
# import sys
# nums = [3, 7, 2, 9, 4, 1]
# max1 = nums[0]
# max2 = - sys.maxsize
# for i in range(1, len(nums)):
#     if nums[i] > max1:
#         temp = max1
#         max1 = nums[i]
#         if temp > max2:
#             max2 = temp
#     elif nums[i] < max1 and nums[i] > max2:
#         max2 = nums[i]
# print(max2)

# -----------------------------------------------------------------------------------------------------------
# Compter les occurrences :

# nums = [1, 2, 2, 3, 1, 4, 2]
# reponse = {1: 2, 2: 3, 3: 1, 4: 1}



# nums = [1, 2, 2, 3, 1, 4, 2]
# reponse = {}

# for num in nums:
#     if num in reponse:
#         reponse[num] = reponse[num] + 1
#     else:
#         reponse[num] = 1
# print(reponse)

# nums = [1, 2, 2, 3, 1, 4, 2]
# reponse = {}

# for num in nums:
#         reponse[num] = reponse.get(num,0) + 1

# print(reponse)

# # -----------------------------------------------------------------------------------------------------------
# Exercice — Trouver le plus fréquent
# Contraintes
# utiliser ton dictionnaire
# pas de max() sur les valeurs
# logique claire (comparaison)

# nums = [1, 2, 2, 3, 1, 4, 2]
# reponses = {}
# for num in nums:
#     reponses[num] = reponses.get(num, 0) +1
# keyMax = 0
# valueMax = 0
# for key, value in reponses.items():
#       if value > valueMax:
#             valueMax = value
#             keyMax = key
# print(keyMax)
# # -----------------------------------------------------------------------------------------------------------
# Retourner les nombres qui apparaissent au moins 2 fois
# Contraintes
# utiliser un dictionnaire
# éviter les doublons dans le résultat
# ordre non important

# nums = [1, 2, 2, 3, 1, 4, 2]
# reponses = {}
# reponseList = []
# for num in nums:
#     reponses[num] = reponses.get(num, 0) +1
# for key , value in reponses.items():
#     if value >= 2:
#         reponseList.append(key)
# print(reponseList)

# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------