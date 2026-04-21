LES DICTIONNAIRES (dict)

Le dictionnaire est l'équivalent du HashMap en Java. Il associe des clés à des valeurs. si on veut garder une cle vide valeur = none

Caractéristique

    Caractéristique							Description										Exemple

    Mutable								Modifiable après création						dict["clé"] = nouvelle_valeur

    Non ordonné (Python < 3.7)			Ordre non garanti										-

    ordonné (Python ≥ 3.7)				Maintient l'ordre d'insertion					Les clés sont dans l'ordre d'ajout

    Clés uniques						Pas de doublon de clés							{"a":1, "a":2} → {"a":2}

    Clés immuables						Les clés doivent être immuables					int, str, tuple, etc.

    Valeurs quelconques					Les valeurs peuvent être n'importe quoi			list, dict, int, str, etc.

    Accès par clé						Pas par index (position)						dict["clé"] et non dict[0]

    Recherche rapide					O(1) en moyenne									Très performant
    
3.1 Créer un dictionnaire

    # Dictionnaire vide
    mon_dict = {}
    mon_dict = dict()

    # Dictionnaire avec des valeurs
    personne = {
        "nom": "Dupont",
        "prenom": "Alice",
        "age": 25,
        "ville": "Paris"
    }

    # Avec dict() et des tuples
    personne = dict([("nom", "Dupont"), ("prenom", "Alice")])

    # Avec des arguments nommés
    personne = dict(nom="Dupont", prenom="Alice", age=25)

    # Les clés peuvent être de différents types (immutables)
    divers = {
        "nom": "Alice",      # clé str
        1: "un",             # clé int
        (1, 2): "coordonnées"  # clé tuple
    }

3.2 Accéder aux valeurs

    personne = {
        "nom": "Dupont",
        "prenom": "Alice",
        "age": 25
    }

    # Accès direct (lève une erreur si la clé n'existe pas)
    print(personne["nom"])     # Dupont
    # print(personne["taille"])  # KeyError !

    # Accès sécurisé avec get (retourne None si la clé n'existe pas)
    print(personne.get("taille"))  # None

    # Avec valeur par défaut
    print(personne.get("taille", "inconnue"))  # inconnue

    # Modifier une valeur
    personne["age"] = 26
    print(personne["age"])     # 26

    # Ajouter une nouvelle paire clé-valeur
    personne["profession"] = "ingénieur"
    print(personne)  # {"nom": "Dupont", "prenom": "Alice", "age": 26, "profession": "ingénieur"}

3.3 Parcourir un dictionnaire

    personne = {
        "nom": "Dupont",
        "prenom": "Alice",
        "age": 25
    }

    # Parcourir les clés
    for cle in personne:
        print(cle)  # nom, prenom, age

    # Parcourir les clés (explicite)
    for cle in personne.keys():
        print(cle)

    # Parcourir les valeurs
    for valeur in personne.values():
        print(valeur)  # Dupont, Alice, 25

    # Parcourir les paires clé-valeur (recommandé)
    for cle, valeur in personne.items():
        print(f"{cle}: {valeur}")

    # Vérifier l'existence d'une clé
    if "nom" in personne:
        print("La clé 'nom' existe")

    if "taille" not in personne:
        print("La clé 'taille' n'existe pas")


3.4 Méthodes des dictionnaires    
    
    personne = {"nom": "Dupont", "prenom": "Alice", "age": 25}

    # Longueur (nombre de paires)
    print(len(personne))  # 3

    # Supprimer une paire (pop retourne la valeur)
    age = personne.pop("age")
    print(age)        # 25
    print(personne)   # {"nom": "Dupont", "prenom": "Alice"}

    # Supprimer avec del
    del personne["prenom"]
    print(personne)   # {"nom": "Dupont"}

    # Supprimer la dernière paire (Python 3.7+)
    # dernier = personne.popitem()

    # Vider le dictionnaire
    personne.clear()
    print(personne)   # {}

    # Copier un dictionnaire
    original = {"a": 1, "b": 2}
    copie = original.copy()        # Copie superficielle
    copie2 = dict(original)        # Autre façon

    # Mettre à jour avec un autre dictionnaire
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    d1.update(d2)
    print(d1)  # {"a": 1, "b": 3, "c": 4}

    # Créer un dictionnaire à partir de listes
    cles = ["nom", "age", "ville"]
    valeurs = ["Alice", 25, "Paris"]
    personne = dict(zip(cles, valeurs))
    print(personne)  # {"nom": "Alice", "age": 25, "ville": "Paris"}  
 
3.5 Dictionnaire avec des valeurs complexes 
    
    # Un dictionnaire peut contenir n'importe quoi
    annuaire = {
        "Alice": {"telephone": "0612345678", "ville": "Paris"},
        "Bob": {"telephone": "0698765432", "ville": "Lyon"},
        "Charlie": {"telephone": "0655555555", "ville": "Marseille"}
    }

    # Accès
    print(annuaire["Alice"]["telephone"])  # 0612345678

    # Parcourir un dictionnaire imbriqué
    for nom, infos in annuaire.items():
        print(f"{nom} habite à {infos['ville']}")

    # Dictionnaire de listes
    notes = {
        "Alice": [15, 14, 16],
        "Bob": [12, 13, 11],
        "Charlie": [18, 17, 19]
    }

    # Calculer la moyenne d'Alice
    moyenne = sum(notes["Alice"]) / len(notes["Alice"])
    print(f"Moyenne d'Alice : {moyenne:.2f}")
    


Copie superficielle : le dictionnaire est nouveau (adresse différente), mais les objets internes sont partagés (même adresse)

Assignation directe (original = copie) : là oui, même adresse

Copie profonde : tout est nouveau (adresses différentes partout)

dict.fromkeys()	list(dict.fromkeys(liste))	conserve l ordre: Oui (Python 3.7+)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    