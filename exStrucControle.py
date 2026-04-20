import random


# Exercice 1 : Pair ou impair

# Demande un nombre à l'utilisateur et affiche s'il est pair ou impair.

# number = int(input("entrez un nombre "))
# if number%2 == 0:
#     print("nombre pair")
# else:
#     print("nombre impair")
# # ----------------------------------------------------------------------------------------------
# Exercice 2 : Maximum de trois nombres
# Demande trois nombres et affiche le plus grand.

# number1 = int(input("donnez un nombre "))

# number2 = int(input("donnez un nombre "))

# number3 = int(input("donnez un nombre "))

# if number1 > number2 and number1 > number3:
#     print(number1)
# elif number2 > number1 and number2 > number3:
#     print(number2)
# elif number3> number1 and number3 > number2:
#     print(number3)
# # # ----------------------------------------------------------------------------------------------
# # Exercice 3 : Année bissextile

# # Demande une année et affiche si elle est bissextile ou non.

# year = int(input("donnez une annee"))

# if year % 4 == 0 and year % 100 != 0:
#     print("ceci est une annee bisextile")
# elif year % 400 == 0:
#     print("anne bisextille")
# # ----------------------------------------------------------------------------------------------
# Exercice 4 : Compte à rebours

# Affiche un compte à rebours de 10 à 1, puis "Décollage !"
# compteur = 10

# while compteur > 0:
#     print(compteur)
#     compteur -= 1
# else:
#     print("decollage")
# # ----------------------------------------------------------------------------------------------
# Exercice 5 : Table de multiplication

# Demande un nombre et affiche sa table de multiplication de 1 à 10.

# number = int(input("donnez un nombre "))
# counter = 0
# while counter <= 10:
#     print(f"{counter} x {number} = {counter * number}")
#     counter += 1
# # ----------------------------------------------------------------------------------------------
# Exercice 6 : Somme des nombres

# Demande un nombre N et affiche la somme de 1 à N.
# number = int(input("donnez un nombre "))
# somme = 0

# while number>0:
#     somme += number
#     number -= 1
# else:
#     print(somme)
# # ----------------------------------------------------------------------------------------------
# Exercice 7 : Nombre secret

# Crée un jeu où l'ordinateur choisit un nombre entre 1 et 100. L'utilisateur doit le deviner. Après chaque essai, afficher "trop grand" ou "trop petit".

# nombreRandom = random.randint(1,100)
# print(nombreRandom)
# reponse = 0
# while nombreRandom != reponse:
#     reponse = int(input("donnez un nombre "))
# else:
#     print("vous avez gagnez")
# # ----------------------------------------------------------------------------------------------
# Exercice 9 : Moyenne des notes

# Demande des notes (l'utilisateur tape "fin" pour arrêter), calcule et affiche la moyenne.

# note = 0 
# reponse = 0
# counter =0
# while reponse != "fin":
#     reponse = input("donnez une note ")
#     if reponse == "fin":
#         break
#     note += int(reponse)
#     counter += 1

# print(f"votre moyenne = {note/counter} ")
# # ----------------------------------------------------------------------------------------------
# Exercice 10 : Triangle d'étoiles

# Demande un nombre N et affiche un triangle d'étoiles de hauteur N :
nombre = int(input("donnez un nombre "))
i=0
j=0
while i< nombre:
    i += 1
    while j < i:
        print("*", end="")
        j += 1
    j = 0
    print()





# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------