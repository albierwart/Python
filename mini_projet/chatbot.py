from operator import itemgetter


def chatbot():
    produits = [
    {"nom": "Nike Air Zoom", "prix": 120, "sport": "course"},
    {"nom": "Adidas Ultraboost", "prix": 150, "sport": "course"},
    {"nom": "Puma Runner", "prix": 90, "sport": "course"},
    
    {"nom": "Nike Metcon", "prix": 130, "sport": "musculation"},
    {"nom": "Reebok Nano", "prix": 110, "sport": "musculation"},
    {"nom": "Adidas Powerlift", "prix": 100, "sport": "musculation"},
    
    {"nom": "Asics Gel Court", "prix": 80, "sport": "tennis"},
    {"nom": "Nike Court Lite", "prix": 70, "sport": "tennis"},
    
    {"nom": "New Balance 574", "prix": 95, "sport": "casual"},
    {"nom": "Vans Old Skool", "prix": 75, "sport": "casual"}
]
    phrase = input("bonjour je suis ton assistant chaussure, quel activité veux tu realiser? ").lower()
    reponses = []
    sport = None
    sports_mots = {
    "course": ["cour", "run", "jogging"],
    "musculation": ["muscu", "gym", "fitness"],
    "tennis": ["tennis"]
}

    trouve = False
    for key,liste in sports_mots.items():
        for mot in liste:
            if mot in phrase:
                sport = key
                trouve = True
                break
        if trouve:
            break
    if not trouve:
        sport = "casual"
    for produit in produits:       
        if produit["sport"] == sport:
            reponses.append(produit)    
    
    budget = int(input("quel budget as tu? "))

    for produit in reponses:
        produit["diff"] = abs(produit["prix"] - budget)   
    reponses.sort(key=itemgetter("diff"))
    if not reponses:
        print("pas de produit a proposer")
    else:
        print("je te propose:")
        indice = 0
        for produit in reponses:
            print(f"-{produit['nom']} au prix de {produit['prix']}€")
            indice += 1
            if indice == 3:
                break
        meilleur_choix = reponses[0]
        if meilleur_choix["prix"] < budget:
            print(f"meilleur choix: {reponses[0]['nom']}({reponses[0]['prix']}€) car en dessous du buget ")
        elif meilleur_choix["prix"] == budget:
            print(f"meilleur choix: {reponses[0]['nom']}({reponses[0]['prix']}€) car egal au buget ")
        elif meilleur_choix["prix"] > budget:
            print(f"meilleur choix: {reponses[0]['nom']}({reponses[0]['prix']}€) au dessus du buget mais qualite meilleur ")