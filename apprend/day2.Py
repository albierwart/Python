
# # Projet : Gestionnaire de tâches (To-Do intelligent)

# liste_tache = [{"nom": "coder", "priorite": "haute", "etat": False},
#                {"nom": "courir", "priorite": "basse", "etat": False}
#                ]


# def aff_tache():
#     indice = 0
#     for tache in liste_tache:
#         indice += 1
#         print(f"{indice } {tache['nom']} - priorité {tache['priorite']}  - {'terminee' if tache['etat'] else 'pas fini'} ")
#     print()

# def ajouter_tache():
#     nom = input("quel tache voulez vous ajoutez? ")
#     prio = input("quel priorite donnez vous a cette tache(haute/basse)")
#     etat = False
#     tache = { "nom" : nom,
#               "priorite" : prio,
#               "etat": etat
#               }
#     liste_tache.append(tache)

# def terminee_nonTerminee():
#     aff_tache()
#     rep = int(input("quel numero de tache voulez vous modifier "))
#     rep = rep-1 
#     rep2 = input("tapez T pour finie ou F pour non finie")
#     while rep2 != "T" and rep2 != "F":
#         rep2 = input("tapez T pour finie ou F pour non finie")
#     if rep2 == "T":
#         liste_tache[rep]['etat'] = True
#     else:
#         liste_tache[rep]['etat'] = False

# def supprimer():
#     aff_tache()
#     rep = int(input("quel numero de tache a supprimer"))
#     rep = rep -1
#     del liste_tache[rep]

# aff_menu = True
# while aff_menu:
#     print("-----Menu-----")
#     print("1 afficher les taches")
#     print("2 ajouter une tache")
#     print("3 marquer une tache comme terminée/ non termminée")
#     print("4 supprimer une tache")
#     print("5 quiter")

#     choix = int(input("quel est votre choix(tapez le chiffre "))
#     print()
#     if choix == 1:
#         aff_tache()
#     elif choix == 2:
#         ajouter_tache()
#     elif choix == 3:
#         terminee_nonTerminee()
#     elif choix == 4:
#         supprimer()
    
#     if choix == 5:
#         aff_menu = False

# ----------------------------------------------------------------------------------------------------------------------------------

# # CALCULATEUR
# liste_operation = {
#     "plus" : "+",
#     "additionner" : "+",
#     "moins" : "-",
#     "soustraire": "-",
#     "multiplier": "*",
#     "fois": "*",
#     "diviser": "/"
    
# }
# def additionner(x, y):
#     return (x+y)
# def soustraction(x,y):
#     return (x-y)
# def multiplication(x,y):
#     return (x*y)
# def division(x,y):
#     if y == 0:
#         return("division par 0 impossible")
#     return (x/y)

# def trouver_variable(liste):
#     operateur = None
#     nombre1 = None
#     nombre2 = None
#     for mot in liste:
#         if mot in liste_operation:
#             if operateur == None:
#                 operateur = liste_operation[mot]
#             else:
#                 print("erreur trop d operateur")
#                 break
#         try:
#             nombre = int(mot)
#             if nombre1 is None:
#                 nombre1 = nombre
#             elif nombre2 is None:
#                 nombre2 = nombre
#             else:
#                 print("erreur trop de nombre")
#                 break
#         except ValueError:
#             continue
#     if nombre1 is None or nombre2 is None or operateur is None:
#         print("calcul impossible")
#         return
#     choix_operation(nombre1, nombre2, operateur)

# def choix_operation(nombre1, nombre2, operateur):
#     if operateur == "+":
#         print(additionner(nombre1, nombre2))
#     elif operateur == "-":
#         print(soustraction(nombre1,nombre2))
#     elif operateur == "*":
#         print(multiplication(nombre1, nombre2))
#     elif operateur == "/":
#         print(division(nombre1,nombre2))
# phrase = input("tapez votre calcul  ")
# liste_mot = phrase.split()
# trouver_variable(liste_mot)



# def additionner(x, y):
#     return (x+y)
# def soustraction(x,y):
#     return (x-y)
# def multiplication(x,y):
#     return (x*y)
# def division(x,y):
#     if y == 0:
#         return("division par 0 impossible")
#     return (x/y)

# liste_operation = {
#     "plus" : additionner,
#     "additionner" : additionner,
#     "moins" : soustraction,
#     "soustraire": soustraction,
#     "multiplier": multiplication,
#     "fois": multiplication,
#     "diviser": division
    
# }
# def trouver_variable(liste):
#     operateur = None
#     nombre1 = None
#     nombre2 = None
#     for mot in liste:
#         if mot in liste_operation:
#             if operateur == None:
#                 operateur = liste_operation[mot]
#             else:
#                 print("erreur trop d operateur")
#                 break
#         try:
#             nombre = int(mot)
#             if nombre1 is None:
#                 nombre1 = nombre
#             elif nombre2 is None:
#                 nombre2 = nombre
#             else:
#                 print("erreur trop de nombre")
#                 break
#         except ValueError:
#             continue
#     if nombre1 is None or nombre2 is None or operateur is None:
#         print("calcul impossible")
#         return
#     resultat = operateur(nombre1,nombre2)
#     print(resultat)



# phrase = input("tapez votre calcul  ")
# liste_mot = phrase.split()
# trouver_variable(liste_mot)



# def additionner(x, y):
#     return (x+y)
# def soustraction(x,y):
#     return (x-y)
# def multiplication(x,y):
#     return (x*y)
# def division(x,y):
#     if y == 0:
#         return("division par 0 impossible")
    
#     return (x/y)

# liste_operation = {
#     "plus" : {"fonction" : additionner, "symbole": "+"},
#     "additionner" : {"fonction" : additionner, "symbole": "+"},
#     "+" : {"fonction" : additionner, "symbole": "+"},
#     "moins" : {"fonction" : soustraction, "symbole": "-"},
#     "soustraire": {"fonction" : soustraction, "symbole": "-"},
#     "-" : {"fonction" : soustraction, "symbole": "-"},
#     "*" : {"fonction" : multiplication, "symbole": "*"},
#     "multiplier": {"fonction" : multiplication, "symbole": "*"},
#     "fois": {"fonction" : multiplication, "symbole": "*"},
#     "diviser": {"fonction" : division, "symbole": "/"},
#     "/" : {"fonction" : division, "symbole": "/"},
    
# }
# historique = []
# def trouver_variable(liste):
#     operateur = None
#     nombre1 = None
#     nombre2 = None
#     symbole = None
#     for mot in liste:
#         if mot in liste_operation:
#             if operateur is None:
#                 operateur = liste_operation[mot]["fonction"]
#                 symbole = liste_operation[mot]["symbole"]
#             else:
#                 print("erreur trop d operateur")
#                 break
#         try:
#             nombre = float(mot)
#             if nombre1 is None:
#                 nombre1 = nombre
#             elif nombre2 is None:
#                 nombre2 = nombre
#             else:
#                 print("erreur trop de nombre")
#                 break
#         except ValueError:
#             continue
#     if nombre1 is None or nombre2 is None or operateur is None:
#         print("calcul impossible")
#         return
#     resultat = operateur(nombre1,nombre2)
#     if resultat != "division par 0 impossible":
#         historique.append(f"{nombre1} {symbole} {nombre2} = {resultat}")
#     print(f"Resultat = {resultat}")

# def aff_historique():
#     for entree in historique:
#         print(entree)


# fonctionne = True
# while fonctionne:
#     phrase = input("tapez votre calcul Q pour terminer H pour historique ")
#     phrase = phrase.lower()
#     if phrase == "h":
#         aff_historique()
#     elif phrase == "q" :
#         fonctionne = False
#     else:
#         liste_mot = phrase.split()
#         trouver_variable(liste_mot)


# def additionner(x, y):
#     return (x+y)
# def soustraction(x,y):
#     return (x-y)
# def multiplication(x,y):
#     return (x*y)
# def division(x,y):
#     if y == 0:
#         return("division par 0 impossible")
    
#     return (x/y)

# liste_operation = {
#     "plus" : {"fonction" : additionner, "symbole": "+"},
#     "additionner" : {"fonction" : additionner, "symbole": "+"},
#     "+" : {"fonction" : additionner, "symbole": "+"},
#     "moins" : {"fonction" : soustraction, "symbole": "-"},
#     "soustraire": {"fonction" : soustraction, "symbole": "-"},
#     "-" : {"fonction" : soustraction, "symbole": "-"},
#     "*" : {"fonction" : multiplication, "symbole": "*"},
#     "multiplier": {"fonction" : multiplication, "symbole": "*"},
#     "fois": {"fonction" : multiplication, "symbole": "*"},
#     "diviser": {"fonction" : division, "symbole": "/"},
#     "/" : {"fonction" : division, "symbole": "/"},
    
# }
# historique = []
# def trouver_variable(liste):
#     operateur = None
#     nombre1 = None
#     nombre2 = None
#     symbole = None
#     for mot in liste:
#         if mot in liste_operation:
#             if operateur is None:
#                 operateur = liste_operation[mot]["fonction"]
#                 symbole = liste_operation[mot]["symbole"]
#             else:
#                 print("erreur trop d operateur")
#                 break
#         try:
#             nombre = float(mot)
#             if nombre1 is None:
#                 nombre1 = nombre
#             elif nombre2 is None:
#                 nombre2 = nombre
#             else:
#                 print("erreur trop de nombre")
#                 break
#         except ValueError:
#             continue
#     if nombre1 is None or nombre2 is None or operateur is None:
#         print("calcul impossible")
#         return
#     resultat = operateur(nombre1,nombre2)
#     if resultat != "division par 0 impossible":
#         historique.append(f"{nombre1} {symbole} {nombre2} = {resultat}")
#     print(f"Resultat = {resultat}")

# def aff_historique():
#     for entree in historique:
#         print(entree)


# fonctionne = True
# while fonctionne:
#     phrase = input("tapez votre calcul Q pour terminer H pour historique ")
#     phrase = phrase.lower()
#     if phrase == "h":
#         aff_historique()
#     elif phrase == "q" :
#         fonctionne = False
#     else:
#         liste_mot = phrase.split()
#         trouver_variable(liste_mot)

 
# def additionner(x, y):
#     return (x+y)
# def soustraction(x,y):
#     return (x-y)
# def multiplication(x,y):
#     return (x*y)
# def division(x,y):
#     if y == 0:
#         return("division par 0 impossible")
    
#     return (x/y)

# liste_operation = {
#     "plus" : {"fonction" : additionner, "symbole": "+"},
#     "additionner" : {"fonction" : additionner, "symbole": "+"},
#     "+" : {"fonction" : additionner, "symbole": "+"},
#     "moins" : {"fonction" : soustraction, "symbole": "-"},
#     "soustraire": {"fonction" : soustraction, "symbole": "-"},
#     "-" : {"fonction" : soustraction, "symbole": "-"},
#     "*" : {"fonction" : multiplication, "symbole": "*"},
#     "multiplier": {"fonction" : multiplication, "symbole": "*"},
#     "fois": {"fonction" : multiplication, "symbole": "*"},
#     "diviser": {"fonction" : division, "symbole": "/"},
#     "/" : {"fonction" : division, "symbole": "/"},
    
# }

# def trouver_variable(liste):
#     print("ok")


# fonctionne = True
# while fonctionne:
#     phrase = input("tapez votre calcul Q pour terminer H pour historique ")
#     phrase = phrase.lower()

#     if phrase == "q" :
#         fonctionne = False
#     else:
#         liste_mot = phrase.split()
#         trouver_variable(liste_mot)   


    

def additionner(liste):
    total = 0
    for number in liste:
        total += number
    return total
def soustraire(liste):
    total = 0
    for number in liste:
        total -= number
    return total
def multiplier(liste):
    total = 1
    for number in liste:
        total = total * number
    return total
def diviser(liste):
    total = list[0]
    for nombre in liste[1:]:
        total = total / nombre
    return total
dico_operation = {
    "+": {"fonction": additionner, "priorite": 1},
    "-": {"fonction": soustraire, "priorite": 1},
    "*": {"fonction": multiplier, "priorite": 2},
    "/": {"fonction": diviser, "priorite": 2},
}  
dico_traducteur = {
    "+": "+",
    "plus" : "+",
    "additionner" : "+",
    "-" : "-",
    "soustraire" : "-",
    "*" : "*",
    "fois" : "*",
    "multiplier" : "*",
    "/" : "/",
    "diviser" : "/"
} 

def trouver_variable(liste):
    numbers = []
    operators = []
    for mot in liste:
        if mot in dico_traducteur:
            operators.append(dico_traducteur[mot])
        try:
            number = float(mot)
            numbers.append(number)
        except ValueError:
            continue
    for i in range(operators):
        

    

fonctionne = True
while fonctionne:
    phrase = input("tapez votre calcul Q pour terminer H pour historique ")
    phrase = phrase.lower()

    if phrase == "q" :
        fonctionne = False
    elif " " in phrase:
        liste_mot = phrase.split()
        trouver_variable(liste_mot)
    else:
        trouver_variable(phrase)