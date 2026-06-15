# Niveau 1 — Projet 1 : Gestionnaire de tâches

def demande_indice_tache(tasks):
    show_task(tasks)
    taille = len(tasks)
    demande = True
    while demande:
        numer = input("quel numero de tache a modifier")
        try:
            num = int(numer)
            if num > 0 and num <= taille:
                return num-1               
            else:
                print("numero invalide")
                continue
        except ValueError:
            print("reponse erronee")
            continue


def show_menu():
    print("************Menu**********")
    print("1: afficher les taches")
    print("2: ajouter une tache")
    print("3: modifier une tache")
    print("4 supprimer une tache")
    print("5: quittez")

def show_task(tasks):
    if not tasks:
        print("pas de tache dans la liste")
    else:
        for i , value in enumerate(tasks):
            print(f"{i+1}: titre: {value['titre']} | priorite: {value['priorite']} | etat: {'terminee' if value['terminee'] else 'pas finie'}")
    print()

def add_task(tasks):
    titre = input("quel est le nom de la tache que vous voulez ajouter? ")
    demande = True
    while demande:
        reponses = ["haute", "moyenne", "basse"]
        priorite = input("quel priorite: haute, moyenne, basse? ")
        priorite = priorite.lower()
        if priorite in reponses:
            demande = False
        else:
            print("reponse attendue: haute, moyenne, basse")
    task = {"titre" : titre,
            "priorite": priorite,
            "terminee" : False
            }
    tasks.append(task)
    print("tache ajoutee")

def edit_task(tasks):
    if not tasks:
        print("pas de tache dans la liste")
        return
    indice_tache= demande_indice_tache(tasks)
    demande = True
    while demande:
        print("quel action faire:")
        print("1: modifier la priorite")
        reponse = input("2: changer l etat (terminee ou pas)? ") 
        match reponse:
            case "1":
                priorite = input("quel est la nouvelle priorite(haute, moyenne,basse)? ")
                tasks[indice_tache]["priorite"] = priorite
                print("modification effectuee")
                demande = False
            case "2":
                tasks[indice_tache]["terminee"] = False if tasks[indice_tache]["terminee"] == True else True
                # autre facon de faire
                # if tasks[indice_tache]["terminee"] is True: 
                #     tasks[indice_tache]["terminee"] = False
                # else:
                #     tasks[indice_tache]["terminee"]= True
                print("modification effectuee")
                demande = False
                
            case _:
                print("reponse incorrecte")
                continue  

def delete_task(tasks):
    if not tasks:
        print("pas de tache dans la liste")
    else:
        indice_tache= demande_indice_tache(tasks)
        del tasks[indice_tache]

def demarrer():
    tasks = []
    on = True
    while on:
        show_menu()
        choice = input("quel est votre choix?")
        match choice:
            case "1":
                show_task(tasks)
            case "2":
                add_task(tasks)
            case "3":
                edit_task(tasks)
            case "4":
                delete_task(tasks)
            case "5":
                on = False
            case _:
                print("mauvaise entree, recommencer")

demarrer()

