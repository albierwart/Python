# Gestionnaire de bibliothèque
# Contexte

# Tu travailles pour une petite bibliothèque municipale.

# Le bibliothécaire souhaite un programme en console permettant de gérer les livres disponibles.


books = [
    {
        "titre": "Le Petit Prince",
        "auteur": "Antoine de Saint-Exupéry",
        "disponible": True
    },
    {
        "titre": "Dune",
        "auteur": "Frank Herbert",
        "disponible": False
    },
    {
        "titre": "1984",
        "auteur": "George Orwell",
        "disponible": True
    },
    {
        "titre": "Fondation",
        "auteur": "Isaac Asimov",
        "disponible": True
    },
    {
        "titre": "Le Seigneur des Anneaux",
        "auteur": "J. R. R. Tolkien",
        "disponible": False
    },
    {
        "titre": "Harry Potter à l'école des sorciers",
        "auteur": "J. K. Rowling",
        "disponible": True
    },
    {
        "titre": "L'Étranger",
        "auteur": "Albert Camus",
        "disponible": True
    },
    {
        "titre": "Les Misérables",
        "auteur": "Victor Hugo",
        "disponible": False
    }
]
liste_menu = ["Afficher les livres", "Ajouter un livre", "Emprunter un livre", "Rendre un livre", "supprimer un livre", "quitter"]


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
        print(f"{indice}. {book['titre']} - {book['auteur']} - {'disponible' if book['disponible'] == True else 'non-disponible'}")

def add_books(books):
    print("vous etes sur le point d ajouter un livre")
    titre = input("quel est le titre du livre? ")
    auteur = input("quel est l auteur? ")
    books.append({"titre" : titre,
           "auteur" : auteur,
           "disponible" : True
           })
    print("le livre a ete ajouté")

def borrow_books(books):
    show_books(books)
    indice = verif_string_is_int(0, len(books))
    indice -=1
    for i in range(len(books)):
        if i == indice and books[i]['disponible'] == True:
            books[i]['disponible'] = False
            print("livre emprunte avec succes")
        elif i == indice and books[i]['disponible'] == False:
            print("livre deja emprunte")


def return_book(books):
    show_books(books)
    indice = verif_string_is_int(0, len(books))
    indice -=1
    for i in range(len(books)):
        if i == indice  and books[i]['disponible'] == False:
            books[i]['disponible'] = True
            print("livre rendu avec succes")
        elif i == indice  and books[i]['disponible'] == True:
            print("ce livre est deja disponible")

def delete_books(books):
    show_books(books)
    indice = indice = verif_string_is_int(0, len(books))
    indice -=1
    for i in range(len(books)):
        if i == indice:
            del books[i]
            print("livre supprime")

def show_menu(debut, fin):
    print("-------------bibliotheque------------------")
    for i in range(debut, fin):
        print(f"{i+1}. {liste_menu[i]}")

def demarrer():
    actif = True
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
                actif = False
            case _:
                print("mauvaise entree, veuillez entrer un chiffre")
demarrer()

