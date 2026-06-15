import json


def save(books):
    with open("projet/niveau2/bibliotheque.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)
        print("donnee sauvegardee")

def charger_donnees():
    try:
        with open("projet/niveau2/bibliotheque.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def verif_string_is_int(debut, fin):
    while True:
        reponse = input(f"veuillez entrez un nombre entier entre {debut} et {fin} ")
        try:
            reponse = int(reponse)
            if debut <= reponse <= fin:
                return reponse
            print(f"veuillez entrez un nombre entier entre {debut} et {fin} ")
        except ValueError:
            print("Réponse erronée.")
    
   

def show_books(books):
    if not books:
        print("aucun livre enregistre") 
    indice = 0
    for book in books:
        indice += 1
        print(f"{indice}. {book['titre']} - {book['auteur']} - {'disponible' if book['disponible'] else 'non-disponible'}")

def add_books(books):
    print("vous etes sur le point d ajouter un livre")
    titre = input("quel est le titre du livre? ")
    auteur = input("quel est l auteur? ")
    books.append({"titre" : titre,
           "auteur" : auteur,
           "disponible" : True
           })
    save(books)
    print("le livre a ete ajouté")

def borrow_books(books):
    show_books(books)
    indice = verif_string_is_int(0, len(books))
    indice -=1
    book = books[indice]
    if book['disponible']:
        book['disponible'] = False
        save(books)
    else:
        print("le livre a deja ete emprunte")

def return_book(books):
    show_books(books)
    indice = verif_string_is_int(0, len(books))-1
    book = books[indice]
    if book['disponible']:
        print("ce livre est deja disponible")
    else:
        book['disponible'] = True
        save(books)
        print("livre rendu avec succes")
    

def delete_books(books):
    show_books(books)
    indice = indice = verif_string_is_int(0, len(books))-1
    del books[indice]
    save(books)
    print("livre supprime")

liste_menu = ["Afficher les livres", "Ajouter un livre", "Emprunter un livre", "Rendre un livre", "supprimer un livre", "quitter"]

def show_menu(debut, fin):
    print("-------------bibliotheque------------------")
    for i in range(debut, fin):
        print(f"{i+1}. {liste_menu[i]}")

def demarrer():
    actif = True
    books = charger_donnees()
    while actif:
        show_menu(0, len(liste_menu))
        choix = input("quel est votre choix(tapez un chiffre)? " )
        match choix:
            case "1":
                show_books(books)
            case "2":
                add_books(books)
            case "3":
                borrow_books(books)
            case "4":
                return_book(books)
            case "5":
                delete_books(books)
            case "6":
                save(books)
                actif = False
            case _:
                print("mauvaise entree, veuillez entrer un chiffre")
demarrer()
