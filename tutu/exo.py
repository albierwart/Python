
# # exo 1
# def Saluer(nom, age):
#     print(f"Bonjour {nom}, vous avez {age} ans.")
# Saluer("alain", 32)

# # exo 2

# def produit(a,b):
#     if a==0 or b==0:
#         print("multiplication par zero detectee")
#         return 0
#     else:
#         return a * b

# exo 3

# carre = []

# for nb in range(1,11):
#     carre.append(nb*nb)

# print(carre)
# #  puis refaites-le en une ligne avec une compréhension de liste. demander un cour

# exo 4

# voyelle = ["a", "e", "i", "o", "u", "y"]

# def compter_voyelle(texte):
#     cpt = 0
#     for letter in texte:
#         if letter in voyelle:
#             cpt +=1
#     return cpt

# print(compter_voyelle("Python"))

# exo 5

# for nb in range(1,21):
#     if nb%3 == 0:
#         print("fizz")
#     elif nb % 5 == 0:
#         print("buzz")
#     else:
#         print(nb)

# exo 6

# def inverser(texte):
#     mot_inverse = ""
#     for lettre in texte:
#         mot_inverse = lettre + mot_inverse
#     print(mot_inverse)

# exo 7 

def convertir_en_fahrenheit(liste_celsius):
    liste_fahrenheit = []
    for nb in liste_celsius:
        liste_fahrenheit.append(nb * (9/5) + 32)
    print(liste_fahrenheit)

# exo 8 

# def maximun(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > c:
#         return b
#     else:
#         return c

# exo 9

def nombre_de_mots(texte):
    mots = texte.split()
    return len(mots)

