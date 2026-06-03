# for i in range(10):
#     if i%2 == 0:
#         print(i)

# nbrNote = int(input("combien de note a encoder"))
# totNote = 0
# for i in range(nbrNote):
#     totNote = totNote + int(input("entrez la note suivante"))
# moyenne = totNote/nbrNote
# print(f"la moyenne est de {moyenne}")
# version alternative:
# nbrNote = int(input("combien de note a encoder"))
# totNote = 0
# for i in range(nbrNote):
#     totNote = totNote + int(input("entrez la note suivante"))
# print(f"la moyenne est de {totNote/nbrNote}")

# def moyenne():
#     nombre_notes = int(input("Combien de notes ? "))
#     total_notes = 0

#     if nombre_notes > 0:
#         for i in range(nombre_notes):
#             note = int(input(f"Entrez la note {i+1} : "))
#             total_notes += note

#         moyenne = total_notes / nombre_notes
#         print(f"La moyenne est de {moyenne}")
#     else:
#         print("Aucune note entrée")
# moyenne()
# def calculMoyenne(liste):
#     total = 0
#     for i in liste:
#         total += i
#     return total/ len(liste)

# def analyser_notes():
#     notes = []
#     reponse = input("donnez la note de l etudiant, tapez fini si plus de note")
#     while(reponse != "fini"):
#         notes.append(int(reponse))
#         reponse = input("donnez la note de l etudiant, tapez fini si plus de note")
#     moyenne  = calculMoyenne(notes)
#     noteMax = max(notes)
#     noteMin = min(notes)
#     resultat = ""
#     if moyenne >= 10:
#         resultat = "reussi"
#     else:
#         resultat = "rate"
#     return print(f"l eleve a une moyenne de {moyenne}, sont meilleur resultat est {noteMax} sa pire note est {noteMin} sont resultat est {resultat}")
    
# produits = [
#     {"nom": "pomme", "prix": 2},
#     {"nom": "banane", "prix": 3},
#     {"nom": "orange", "prix": 4}
# ]
# total = 0
# for i in produits:
#     print(f"{i["nom"]} - {i["prix"]}€")
#     total += i["prix"]
# print(f"total = {total}")

    
# produits = [
#     {"nom": "pomme", "prix": 2, "promo":True},
#     {"nom": "banane", "prix": 3, "promo":False},
#     {"nom": "orange", "prix": 4, "promo":True}
# ]
# total = 0
# for i in produits:
#     if i["promo"] == True:
#         print(f"{i["nom"]} - {i["prix"]/2}€")
#         total += i["prix"]/2
#     else:
#         print(f"{i["nom"]} - {i["prix"]}€")
#         total += i["prix"]
# print(f"total = {total}")

    
# produits = [
#     {"nom": "pomme", "prix": 2, "promo":True},
#     {"nom": "banane", "prix": 3, "promo":False},
#     {"nom": "orange", "prix": 4, "promo":True}
# ]

# for produit in produits:
#     if produit["promo"] :
#         print(f"{produit["nom"]} - {produit["prix"]/2}€")
# i = {"nom": "pomme"}
# print(f"{i["nom"]}")

# db = {"nom": "nike run", "prix": 100, "sport": "course"}
# sport = input("quel sport? ")
# if sport == "course":
#     print(db["nom"])

# produits = [
#     {"nom": "nike run", "prix": 100, "sport": "course"},
#     {"nom": "adidas gym", "prix": 80, "sport": "musculation"},
#     {"nom": "puma run", "prix": 90, "sport": "course"}
# ]

# sport = input("quel sport pratiquez vous? ")

# for produit in produits:
#     if sport == produit["sport"]:
#         print(produit["nom"])

# produits = [
#     {"nom": "nike run", "prix": 100, "sport": "course"},
#     {"nom": "adidas gym", "prix": 80, "sport": "musculation"},
#     {"nom": "puma run", "prix": 90, "sport": "course"}
# ]

# sport = input("quel sport pratiquez vous? ").lower()
# trouve = False
# for produit in produits:
#     if sport == produit["sport"]:
#         print(produit["nom"])
#         trouve = True
# if not trouve:
#     print("aucun article trouve")
# produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
# sport = input("quel sport? ").lower()
# budget = int(input("quel budget "))
# reponse = {}
# for produit in produits:
#     if sport == produit["sport"] and  produit["prix"]<= budget :
#         if not reponse:
#             reponse = produit
#         elif produit["prix"] < reponse["prix"]:
#             reponse = produit
# print(reponse["nom"])

# produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
# sport = input("quel sport? ").lower()
# budget = int(input("quel budget "))
# reponse = None
# for produit in produits:
#     if sport == produit["sport"] and  produit["prix"]<= budget :
#         if reponse is None:
#             reponse = produit
#         elif produit["prix"] < reponse["prix"]:
#             reponse = produit
# if reponse:
#     print(reponse["nom"])
# else:
#     print("Aucun produit trouvé")

# produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
# sport = input("quel sport? ").lower()
# budget = int(input("quel budget "))
# choix = input("moins cher ou plus cher")
# reponse = None
# for produit in produits:
#     if choix == "moins cher":
#         if sport == produit["sport"] and  produit["prix"]<= budget :
#             if reponse is None:
#                 reponse = produit
#             elif produit["prix"] < reponse["prix"]:
#                 reponse = produit
#     else:
#         if sport == produit["sport"] and  produit["prix"]<= budget :
#             if reponse is None:
#                 reponse = produit
#             elif produit["prix"] > reponse["prix"]:
#                 reponse = produit
# if reponse:
#     print(reponse["nom"])
# else:
#     print("Aucun produit trouvé")
# import sys
# produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
# sport = input("quel sport? ").lower()
# budget = int(input("quel budget "))
# choix = input("moins cher ou plus cher")
# reponse = None
# diff = sys.maxsize

# for produit in produits:
#     if produit["sport"]== sport:
#         if reponse is None:
#             reponse = produit
#         diffProduit = abs(produit["prix"]- budget)
#         if diffProduit < diff:
#             diff = diffProduit
#             reponse = produit
# print(reponse)

# import sys
# produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
# sport = input("quel sport? ").lower()
# budget = int(input("quel budget "))
# reponse = None
# diff = sys.maxsize

# for produit in produits:
#     if produit["sport"]== sport:       
#         diffProduit = abs(produit["prix"]- budget)
#         if diffProduit < diff:
#             diff = diffProduit
#             reponse = produit
# if reponse is None:
#     print("pas de reponse")
# else:
#     print(f"Je te recommande : {reponse['nom']} à {reponse['prix']}€")

# import sys

# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
#     print("bonjour je suis ton assistant chaussure")
#     sport = input("quel sport pratiques tu? ").lower()
#     budget = int(input("quel est ton budget?"))   
#     reponse = None
#     diff = sys.maxsize

#     for produit in produits:
#         diffProduit = abs(produit["prix"] - budget)
#         if produit["sport"] == sport and diffProduit < diff:
#             diff = diffProduit
#             reponse = produit
#     if reponse is None:
#         print("pas de produit trouvé")
#     else:
#         print(f"je te propose {reponse['nom']} au prix de {reponse['prix']}€")

# chatbot()

# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
    
#     phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ")
#     budget = int(input("quel budget as tu? "))
#     reponse = None
#     diff = 1000
#     sport = None
#     if "cour" in phrase or "course" in phrase or "running" in phrase:
#         sport = "course"
#     elif "muscu" in phrase:
#         sport = "musculation"
#     elif "tennis" in phrase:
#         sport = "tennis"
#     else:
#         print("je n ai pas compris alors je te propose des chaussures casual")
#         sport = "casual"
#     for produit in produits:
#         diffProduit = abs(produit["prix"] - budget)
#         if produit["sport"] == sport and diffProduit < diff:
#             reponse = produit
#             diff = diffProduit
#     if reponse is None:
#         print("pas de produit a proposer")
#     else:
#         print(f"je te propose {reponse["nom"]} au prix de {reponse["prix"]}€")
     

# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
#     phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ").lower()
#     budget = int(input("quel budget as tu? "))
#     reponse = None
#     diff = 1000
#     sport = None
#     mots_course = ["cour", "run", "jogging"]
#     mots_muscu = ["muscu", "gym", "fitness"]
#     mots_tennis = ["tennis"]

#     for mot in phrase:
#         if mot in mots_course:
#             sport = "course"
#         elif mot in mots_muscu:
#             sport = "musculation"
#         elif mot in mots_tennis:
#             sport = "tennis"
#     else:
#         sport = "casual"
#     for produit in produits:
#         diffProduit = abs(produit["prix"] - budget)
#         if produit["sport"] == sport and diffProduit < diff:
#             reponse = produit
#             diff = diffProduit
#     if reponse is None:
#         print("pas de produit a proposer")
#     else:
#         print(f"je te propose {reponse["nom"]} au prix de {reponse["prix"]}€")

# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
#     phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ").lower()
#     budget = int(input("quel budget as tu? "))
#     reponse = None
#     diff = 1000
#     sport = None
#     sports_mots = {
#     "course": ["cour", "run", "jogging"],
#     "musculation": ["muscu", "gym", "fitness"],
#     "tennis": ["tennis"]
# }
#     trouve = False
#     for key,liste in sports_mots.items():
#         for mot in liste:
#             if mot in phrase:
#                 sport = key
#                 trouve = True
#                 break
#         if trouve:
#             break
#     if not trouve:
#         sport = "casual"

#     for produit in produits:
#         diffProduit = abs(produit["prix"] - budget)
#         if produit["sport"] == sport and diffProduit < diff:
#             reponse = produit
#             diff = diffProduit
#     if reponse is None:
#         print("pas de produit a proposer")
#     else:
#         print(f"je te propose {reponse['nom']} au prix de {reponse['prix']}€")

# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course", "budget": "moyen"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course", "budget": "grand"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course", "budget": "moyen"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation", "budget": "grand"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation", "budget": "moyen"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation", "budget": "moyen"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis", "budget": "petit"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis", "budget": "petit"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual", "budget": "moyen"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual", "budget": "petit"}
# ]
#     phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ").lower()
#     reponse = []
#     sport = None
#     sports_mots = {
#     "course": ["cour", "run", "jogging"],
#     "musculation": ["muscu", "gym", "fitness"],
#     "tennis": ["tennis"]
# }

#     trouve = False
#     for key,liste in sports_mots.items():
#         for mot in liste:
#             if mot in phrase:
#                 sport = key
#                 trouve = True
#                 break
#         if trouve:
#             break
#     if not trouve:
#         sport = "casual"
    
#     budget = int(input("quel budget as tu? "))
#     if budget < 80:
#         budget = "petit"
#     elif budget <121:
#         budget = "moyen"
#     else:
#         budget = "grand"

#     for produit in produits:        
#         if produit["sport"] == sport and produit["budget"] == budget:
#             reponse.append(produit)             
    
    
#     if not reponse:
#         print("pas de produit a proposer")
#     else:
#         print("je te propose:")
#         for produit in reponse:
#             print(f"-{produit['nom']} au prix de {produit['prix']}€")
# from operator import itemgetter

# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course", "budget": "moyen"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course", "budget": "grand"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course", "budget": "moyen"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation", "budget": "grand"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation", "budget": "moyen"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation", "budget": "moyen"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis", "budget": "petit"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis", "budget": "petit"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual", "budget": "moyen"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual", "budget": "petit"}
# ]
#     phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ").lower()
#     reponse = []
#     sport = None
#     sports_mots = {
#     "course": ["cour", "run", "jogging"],
#     "musculation": ["muscu", "gym", "fitness"],
#     "tennis": ["tennis"]
# }

#     trouve = False
#     for key,liste in sports_mots.items():
#         for mot in liste:
#             if mot in phrase:
#                 sport = key
#                 trouve = True
#                 break
#         if trouve:
#             break
#     if not trouve:
#         sport = "casual"
    
#     budget = int(input("quel budget as tu? "))
#     if budget < 80:
#         budget = "petit"
#     elif budget <121:
#         budget = "moyen"
#     else:
#         budget = "grand"

#     for produit in produits:        
#         if produit["sport"] == sport and produit["budget"] == budget:
#             reponse.append(produit)             
    
#     reponse.sort(key=itemgetter("prix"))
#     if not reponse:
#         print("pas de produit a proposer")
#     else:
#         print("je te propose:")
#         for produit in reponse:
#             print(f"-{produit['nom']} au prix de {produit['prix']}€")

# from operator import itemgetter

# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
#     phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ").lower()
#     reponse = []
#     sport = None
#     sports_mots = {
#     "course": ["cour", "run", "jogging"],
#     "musculation": ["muscu", "gym", "fitness"],
#     "tennis": ["tennis"]
# }

#     trouve = False
#     for key,liste in sports_mots.items():
#         for mot in liste:
#             if mot in phrase:
#                 sport = key
#                 trouve = True
#                 break
#         if trouve:
#             break
#     if not trouve:
#         sport = "casual"
    
#     budget = int(input("quel budget as tu? "))
#     diff = 10000000000000
#     for produit in produits:  
#         diffProduit = abs(produit["prix"]-budget)      
#         if produit["sport"] == sport and diffProduit < diff:
#             diff = diffProduit
#             reponse.append(produit)             
    
#     reponse.sort(key=itemgetter("prix"))
#     if not reponse:
#         print("pas de produit a proposer")
#     else:
#         print("je te propose:")
#         indice = 0
#         for produit in reponse:
#             print(f"-{produit['nom']} au prix de {produit['prix']}€")
#             indice += 1
#             if indice == 3:
#                 break



# from operator import itemgetter


# def chatbot():
#     produits = [
#     {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
#     {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
#     {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
#     {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
#     {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
#     {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
#     {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
#     {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
#     {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
#     {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
# ]
#     phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ").lower()
#     reponses = []
#     sport = None
#     sports_mots = {
#     "course": ["cour", "run", "jogging"],
#     "musculation": ["muscu", "gym", "fitness"],
#     "tennis": ["tennis"]
# }

#     trouve = False
#     for key,liste in sports_mots.items():
#         for mot in liste:
#             if mot in phrase:
#                 sport = key
#                 trouve = True
#                 break
#         if trouve:
#             break
#     if not trouve:
#         sport = "casual"
#     for produit in produits:       
#         if produit["sport"] == sport:
#             reponses.append(produit)    
    
#     budget = int(input("quel budget as tu? "))

#     for produit in reponses:
#         produit["diff"] = abs(produit["prix"] - budget)   
#     reponses.sort(key=itemgetter("diff"))
#     if not reponses:
#         print("pas de produit a proposer")
#     else:
#         print("je te propose:")
#         indice = 0
#         for produit in reponses:
#             print(f"-{produit['nom']} au prix de {produit['prix']}€")
#             indice += 1
#             if indice == 3:
#                 break
#         meilleur_choix = reponses[0]
#         if meilleur_choix["prix"] < budget:
#             print(f"meilleur choix: {reponses[0]['nom']}({reponses[0]['prix']}€) car en dessous du buget ")
#         elif meilleur_choix["prix"] == budget:
#             print(f"meilleur choix: {reponses[0]['nom']}({reponses[0]['prix']}€) car egal au buget ")
#         elif meilleur_choix["prix"] > budget:
#             print(f"meilleur choix: {reponses[0]['nom']}({reponses[0]['prix']}€) au dessus du buget mais qualite meilleur ")