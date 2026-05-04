# print("bonjour je reviens")
# prenom = "alain"
# print(f"bonjour {prenom}")
# age = input("quel age as tu? ")
# print(f"{prenom} a comme age: {age}")
# nbr1 = int(input("entrez un nbr"))
# nbr2 = int(input("entrez le nbr2"))
# print(f"la somme = {nbr1+nbr2}")
# liste = list()
# for nbr in range(0,2):
#     liste.append(int(input("entrez un nbr ")))
# somme = liste[0]+liste[1]
# print(somme)
# nbr = int(input("donnez un nbr "))
# for n in range(1,nbr+1):
#     print(n)
# liste= ["pomme", "bananne", "orange"]
# liste.append("noix")
# print(liste)

# Exercice 11 : Somme d'une liste

# Demande à l'utilisateur de taper 5 nombres, stocke-les dans une liste, puis affiche leur somme.
liste = []
# for i in range(5):
#     liste.append(int(input("entrez un nbr ")))
# print(liste)
# somme =0
# for n in liste:
#     somme += n
# print(somme)

# Exercice 12 : Plus grand d'une liste

# À partir de la liste de l'exercice 11, affiche le plus grand nombre (sans utiliser max()).
# maxi = 0
# for n in liste:
#     if n > maxi:
#         maxi=n
# # print(maxi)
# Exercice 13 : Compte à rebours

# Affiche un compte à rebours de 10 à 0, puis affiche "Décollage !".

# cpt = 10
# while(cpt>0):
#     print(cpt)
#     cpt-=1
#     if cpt == 0:
#         print("decollage")

# Exercice 14 : Devine le nombre

# L'ordinateur choisit un nombre entre 1 et 20. L'utilisateur doit le deviner. Après chaque essai, affiche "plus grand" ou "plus petit".
# import random

# nbr_secret = random.randint(1,20)
# reponse = 0
# print(nbr_secret)
# while(reponse != nbr_secret):
#     reponse = int(input("entrez un nbr "))
#     if reponse < nbr_secret:
#         print("plus grand")
#     else:
#         print("plus petit")
# else:
#     print("nbr secret trouvé")