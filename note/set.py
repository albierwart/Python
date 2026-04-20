PARTIE 4 : LES ENSEMBLES (set)

L'ensemble est une collection non ordonnée d'éléments uniques.

4.1 Créer un ensemble

    # Ensemble vide
    mon_set = set()  # Attention : {} est un dictionnaire vide !

    # Ensemble avec des valeurs
    fruits = {"pomme", "banane", "orange"}

    # À partir d'une liste (supprime les doublons)
    nombres = set([1, 2, 2, 3, 3, 3, 4])
    print(nombres)  # {1, 2, 3, 4}

    # À partir d'une chaîne
    lettres = set("bonjour")
    print(lettres)  # {'b', 'o', 'n', 'j', 'u', 'r'} (ordre aléatoire)

4.2 Opérations sur les ensembles

    # Ajouter un élément
    fruits = {"pomme", "banane"}
    fruits.add("orange")
    print(fruits)  # {"pomme", "banane", "orange"}

    # Ajouter plusieurs éléments
    fruits.update(["kiwi", "mangue"])
    print(fruits)  # {"pomme", "banane", "orange", "kiwi", "mangue"}

    # Supprimer un élément (erreur si n'existe pas)
    fruits.remove("banane")

    # Supprimer un élément (pas d'erreur si n'existe pas)
    fruits.discard("cerise")  # Ne fait rien

    # Supprimer un élément arbitraire (et le retourner)
    element = fruits.pop()

    # Vider l'ensemble
    fruits.clear()

    # Vérifier l'appartenance
    if "pomme" in fruits:
        print("La pomme est dans l'ensemble")
    
4.3 Opérations mathématiques sur les ensembles

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    # Union : éléments présents dans a OU b
    print(a | b)           # {1, 2, 3, 4, 5, 6}
    print(a.union(b))      # Pareil

    # Intersection : éléments présents dans a ET b
    print(a & b)           # {3, 4}
    print(a.intersection(b))

    # Différence : éléments dans a mais pas dans b
    print(a - b)           # {1, 2}
    print(a.difference(b))

    # Différence symétrique : éléments dans a ou b mais pas les deux
    print(a ^ b)           # {1, 2, 5, 6}
    print(a.symmetric_difference(b))

    # Sous-ensemble (tous les éléments de a sont dans b)
    print(a <= b)          # False
    print({1, 2}.issubset({1, 2, 3}))  # True

    # Sur-ensemble (b contient tous les éléments de a)
    print(a >= b)          # False
    print({1, 2, 3}.issuperset({1, 2}))  # True

    # Ensembles disjoints (aucun élément commun)
    print(a.isdisjoint({5, 6, 7}))  # False (3 et 4 sont dans a et b)


4.4 Utilité pratique des ensembles

    # 1. Supprimer les doublons d'une liste
    ma_liste = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    sans_doublons = list(set(ma_liste))
    print(sans_doublons)  # [1, 2, 3, 4, 5] (ordre non garanti)

    # 2. Trouver les éléments communs à deux listes
    liste1 = [1, 2, 3, 4, 5]
    liste2 = [4, 5, 6, 7, 8]
    communs = set(liste1) & set(liste2)
    print(communs)  # {4, 5}

    # 3. Vérifier si une liste contient des doublons
    def contient_doublons(liste):
        return len(liste) != len(set(liste))

    print(contient_doublons([1, 2, 3, 4]))    # False
    print(contient_doublons([1, 2, 3, 2]))    # True

    # 4. Ensemble de mots uniques dans un texte
    texte = "le chat le chien le chat oiseau"
    mots_uniques = set(texte.split())
    print(mots_uniques)  # {'le', 'chat', 'chien', 'oiseau'}