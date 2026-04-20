fonction unpacking

Excellent ! Je vais vous expliquer en détail le unpacking (dépaquetage) d'arguments en Python.
Pourquoi * et ** ?

Voici quand utiliser le unpacking de façon concise :

    1. Pour appeler une fonction : quand vous avez déjà une liste ou un dictionnaire et que vous voulez passer son contenu comme arguments séparés, sans avoir à écrire chaque élément un par un.

    2. Pour fusionner des collections : quand vous voulez combiner plusieurs listes en une seule, ou plusieurs dictionnaires en un seul, de manière rapide et lisible.

    3. Pour assigner des variables : quand vous voulez extraire les éléments d'une séquence dans des variables distinctes,
    surtout si vous ne voulez récupérer que certains éléments et ignorer les autres.

    4. Pour retourner des valeurs : quand une fonction retourne une séquence et que vous voulez directement la répartir dans plusieurs variables.

    En résumé : utilisez le unpacking chaque fois que vous devez convertir une structure de données en éléments individuels, 
    que ce soit pour les passer à une fonction, les fusionner, ou les stocker dans des variables séparées.

Le nombre d'astérisques correspond au type de structure à dépaqueter :

    * (1 astérisque) → pour les séquences itérables : listes, tuples, chaînes, ensembles

    ** (2 astérisques) → pour les dictionnaires (clés-valeurs)

    1. * pour les séquences (listes, tuples, etc.)
    Principe : transformer une liste en arguments individuels


    def additionner(a, b, c):
        return a + b + c

    # Sans unpacking (manuel)
    nombres = [10, 20, 30]
    resultat = additionner(nombres[0], nombres[1], nombres[2])  # Fastidieux

    # Avec unpacking (automatique)
    resultat = additionner(*nombres)  # * dépaquette → 10, 20, 30
    print(resultat)  # 60

    Ce qui se passe exactement :


    nombres = [10, 20, 30]
    additionner(*nombres)

    # Python transforme *nombres en :
    additionner(10, 20, 30)

    Exemples avec différents types de séquences


    # Avec un tuple
    def saluer(prenom, nom):
        print(f"Bonjour {prenom} {nom}")

    personne = ("Jean", "Dupont")
    saluer(*personne)  # Bonjour Jean Dupont

    # Avec une chaîne de caractères
    def afficher_lettres(a, b, c):
        print(f"1: {a}, 2: {b}, 3: {c}")

    mot = "XYZ"
    afficher_lettres(*mot)  # 1: X, 2: Y, 3: Z

    # Avec un set (mais l'ordre n'est pas garanti)
    def calculer(x, y):
        return x * y

    valeurs = {5, 3}  # set
    print(calculer(*valeurs))  # 15 (peut être 5*3 ou 3*5)

    Attention au nombre d'arguments !
    python

    def additionner(a, b, c):
        return a + b + c

    # Erreur : pas assez d'éléments
    nombres = [10, 20]
    additionner(*nombres)  # TypeError: missing 1 required positional argument

    # Erreur : trop d'éléments
    nombres = [10, 20, 30, 40]
    additionner(*nombres)  # TypeError: takes 3 positional arguments but 4 were given

2. ** pour les dictionnaires
    Principe : transformer un dictionnaire en arguments nommés


    def afficher_personne(nom, age, ville):
        print(f"{nom}, {age} ans, {ville}")

# Sans unpacking
    infos = {"nom": "Alice", "age": 25, "ville": "Paris"}
    afficher_personne(infos["nom"], infos["age"], infos["ville"])  # Fastidieux

# Avec unpacking
    afficher_personne(**infos)  # ** dépaquette → nom="Alice", age=25, ville="Paris"

    Ce qui se passe exactement :


    infos = {"nom": "Alice", "age": 25, "ville": "Paris"}
    afficher_personne(**infos)

# Python transforme **infos en :
    afficher_personne(nom="Alice", age=25, ville="Paris")

    Les clés doivent correspondre aux paramètres

    def afficher_personne(nom, age, ville):
        print(f"{nom}, {age} ans, {ville}")

# Correct
    infos = {"nom": "Alice", "age": 25, "ville": "Paris"}
    afficher_personne(**infos)  # ✅

# Erreur : clé incorrecte
    infos = {"name": "Alice", "age": 25, "ville": "Paris"}  # "name" au lieu de "nom"
    afficher_personne(**infos)  # TypeError: got an unexpected keyword argument 'name'

# Erreur : clé manquante
    infos = {"nom": "Alice", "age": 25}  # manque "ville"
    afficher_personne(**infos)  # TypeError: missing required argument 'ville'

Cas pratiques avancés
        1. Mélanger arguments normaux et unpacking

            def presentation(nom, age, pays="France"):
            print(f"{nom}, {age} ans, de {pays}")

            infos = {"age": 25, "pays": "Belgique"}
            presentation("Pierre", **infos)  # Pierre, 25 ans, de Belgique

    2. Combiner * et **

        def tout_afficher(a, b, c, x, y):
            print(f"a={a}, b={b}, c={c}, x={x}, y={y}")

        liste = [1, 2, 3]
        dico = {"x": 4, "y": 5}
        tout_afficher(*liste, **dico)  # a=1, b=2, c=3, x=4, y=5

    3. Unpacking partiel

        def fonction(a, b, c):
        print(a, b, c)

# Avec une liste plus grande (on peut prendre une partie)
        valeurs = [1, 2, 3, 4, 5]
        fonction(*valeurs[:3])  # 1 2 3

# Ou avec l'opérateur * dans l'appel
        fonction(1, *[2, 3])  # 1 2 3

    4. Copier des listes/dictionnaires

# Copier une liste
        original = [1, 2, 3]
        copie = [*original]  # [1, 2, 3]
        print(copie)  # [1, 2, 3]

# Fusionner des listes
        liste1 = [1, 2, 3]
        liste2 = [4, 5, 6]
        fusion = [*liste1, *liste2]  # [1, 2, 3, 4, 5, 6]

# Fusionner des dictionnaires
        dico1 = {"a": 1, "b": 2}
        dico2 = {"c": 3, "d": 4}
        fusion_dico = {**dico1, **dico2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    Tableau récapitulatif
        Opérateur	Utilisation	Dépaquette	Exemple
        *	Arguments positionnels	Liste, tuple, string, set	fonction(*[1,2,3]) → fonction(1,2,3)
        **	Arguments nommés	Dictionnaire	fonction(**{'a':1, 'b':2}) → fonction(a=1, b=2)
    Erreurs courantes

# 1. Confondre * et **
        dico = {"a": 1, "b": 2}
        fonction(*dico)  # Envoie les CLÉS ('a', 'b'), pas les valeurs
        fonction(**dico)  # Envoie a=1, b=2 ✅

# 2. Oublier que les clés doivent correspondre
        def test(nom, age): pass
        infos = {"name": "Alice", "age": 25}
        test(**infos)  # Erreur: 'name' n'est pas un paramètre

# 3. Nombre d'éléments incorrect
        def somme(a, b): return a + b
        somme(*[1, 2, 3])  # Erreur: trop d'arguments

Analogie pour comprendre

    Imaginez que vous avez une boîte avec des objets :

        * = vider la boîte et disposer les objets un par un sur la table

        ** = étiqueter les objets avant de les disposer sur la table



# Boîte = liste [10, 20, 30]
        def poser(a, b, c): ...
        poser(*boite)  # → poser(10, 20, 30)

# Boîte = dictionnaire {"nom": "Alice", "age": 25}
        def presenter(nom, age): ...
        presenter(**boite)  # → presenter(nom="Alice", age=25)

En résumé : * pour les listes/tuples (positionnel), ** pour les dictionnaires (nommé) !