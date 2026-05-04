COURS COMPLET : PROGRAMMATION ORIENTÉE OBJET (POO)
Introduction : Pourquoi la POO ?
Le problème du code procédural

Imagine que tu dois gérer une bibliothèque. En programmation procédurale (ce qu'on a fait jusqu'ici), tu aurais :
python

# Version procédurale (sans objets)
livres_titres = ["1984", "Dune", "Le Petit Prince"]
livres_auteurs = ["Orwell", "Herbert", "Saint-Exupéry"]
livres_annees = [1949, 1965, 1943]
livres_disponibles = [True, True, True]

def emprunter_livre(titre):
    # Il faut trouver l'index du titre
    # Puis modifier livres_disponibles au même index
    # Et si un jour on ajoute un éditeur ? Il faut ajouter une nouvelle liste...

Problèmes :

    Les données sont éparpillées dans plusieurs listes

    Les fonctions et les données sont déconnectées

    Si on ajoute un nouvel attribut (ex: editeur), il faut modifier toutes les fonctions

    Le code devient difficile à lire et à maintenir

La solution : la Programmation Orientée Objet

La POO dit : regroupons les données ET les fonctions qui agissent sur ces données dans une même structure : un objet.
python

class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Vous avez emprunté {self.titre}")
        else:
            print(f"{self.titre} n'est pas disponible")
    
    def retourner(self):
        self.disponible = True
        print(f"Merci d'avoir rendu {self.titre}")

Avantages :

    Toutes les informations sur un livre sont regroupées au même endroit

    Le livre "sait" comment s'emprunter et se retourner

    Pour ajouter un attribut (ex: editeur), on modifie une seule classe

    Le code est plus naturel : on parle à des objets comme dans la vie réelle

PARTIE 1 : CLASSES ET OBJETS
1.1 Classe vs Objet : l'analogie du moule à gâteaux

Prenons une analogie simple :

    Une classe = un moule à gâteaux (le plan, le modèle)

    Un objet = un gâteau fabriqué à partir de ce moule

Le moule (la classe) définit la FORME que vont avoir tous les gâteaux. Mais chaque gâteau (objet) peut avoir ses propres caractéristiques : un gâteau au chocolat, un autre à la vanille.
python

# La classe = le moule
class Gateau:
    def __init__(self, parfum):
        self.parfum = parfum

# Les objets = les gâteaux créés à partir du moule
gateau_chocolat = Gateau("chocolat")
gateau_vanille = Gateau("vanille")

print(gateau_chocolat.parfum)  # chocolat
print(gateau_vanille.parfum)   # vanille

1.2 Qu'est-ce qu'une classe ?

Une classe est un plan qui définit :

    Les attributs : ce que l'objet a (ex: une voiture a une marque, un modèle)

    Les méthodes : ce que l'objet sait faire (ex: une voiture peut démarrer, rouler)

python

# Définition d'une classe
class Voiture:
    pass  # "pass" signifie "rien pour l'instant"

# Création d'objets (instances)
ma_voiture = Voiture()
ta_voiture = Voiture()

print(type(ma_voiture))  # <class '__main__.Voiture'>

Pour l'instant, notre classe Voiture est vide. Un objet de type Voiture existe, mais il n'a ni attribut ni méthode. C'est une coquille vide.
1.3 Le constructeur __init__

Le constructeur est une méthode spéciale qui est appelée automatiquement quand on crée un nouvel objet. Son rôle est d'initialiser l'objet.
python

class Voiture:
    def __init__(self, marque, modele, annee):
        """Constructeur : appelé automatiquement à la création"""
        # self = l'objet qu'on est en train de créer
        # marque, modele, annee = les paramètres qu'on reçoit
        self.marque = marque      # On attache marque à l'objet
        self.modele = modele      # On attache modele à l'objet
        self.annee = annee        # On attache annee à l'objet
        self.kilometrage = 0      # Valeur par défaut (pas besoin de paramètre)

# Création d'un objet : Python appelle automatiquement __init__
voiture1 = Voiture("Tesla", "Model 3", 2024)
# Détail de ce qui se passe :
# 1. Python crée un objet vide
# 2. Python appelle __init__(objet_vide, "Tesla", "Model 3", 2024)
# 3. À l'intérieur de __init__, "self" est l'objet vide
# 4. On lui ajoute des attributs : marque, modele, annee, kilometrage
# 5. L'objet initialisé est retourné et stocké dans voiture1

print(voiture1.marque)   # Tesla
print(voiture1.modele)   # Model 3
print(voiture1.annee)    # 2024
print(voiture1.kilometrage)  # 0

Pourquoi self ?

self est le nom conventionnel (on pourrait l'appeler autrement, mais ne le faites pas) qui représente l'objet lui-même à l'intérieur de la classe. C'est l'équivalent de this en Java.
python

class Exemple:
    def __init__(self, valeur):
        self.ma_valeur = valeur  # "self" = l'objet qu'on construit
    
    def afficher(self):
        print(self.ma_valeur)     # "self" = l'objet qui appelle la méthode

obj = Exemple(42)
obj.afficher()  # Python transforme automatiquement en Exemple.afficher(obj)

1.4 Les méthodes d'instance

Une méthode est une fonction qui appartient à une classe. Elle s'appelle sur un objet spécifique.
python

class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0
    
    def demarrer(self):
        """Cette méthode agit sur l'objet (self)"""
        print(f"{self.marque} {self.modele} démarre ! Vroum vroum !")
    
    def rouler(self, km):
        """Modifie l'état de l'objet"""
        self.kilometrage += km
        print(f"Vous avez parcouru {km} km. Total : {self.kilometrage} km")
    
    def afficher_infos(self):
        """Affiche l'état actuel de l'objet"""
        print(f"{self.marque} {self.modele} - {self.annee} - {self.kilometrage} km")

# Utilisation
ma_voiture = Voiture("Peugeot", "208", 2022)

# Appel de méthode : l'objet avant le point
ma_voiture.demarrer()      # "ma_voiture" devient "self" à l'intérieur
ma_voiture.rouler(50)      # ma_voiture.kilometrage passe de 0 à 50
ma_voiture.rouler(30)      # ma_voiture.kilometrage passe de 50 à 80
ma_voiture.afficher_infos()

Ce qui se passe :

    Quand on écrit ma_voiture.demarrer(), Python transforme en Voiture.demarrer(ma_voiture)

    ma_voiture devient donc self dans la méthode

    La méthode peut ainsi accéder aux attributs de ma_voiture via self

PARTIE 2 : ATTRIBUTS DE CLASSE VS ATTRIBUTS D'INSTANCE
2.1 Comprendre la différence

Imagine une école. Dans cette école :

    Chaque élève a son propre nom, son propre âge, sa propre note → attributs d'instance

    Tous les élèves partagent le même nom d'école, le même numéro de SIRET → attributs de classe

python

class Eleve:
    # Attribut de classe : partagé par TOUS les élèves
    nom_ecole = "Python School"
    compteur_eleves = 0
    
    def __init__(self, nom, age):
        # Attributs d'instance : propres à CHAQUE élève
        self.nom = nom
        self.age = age
        # On incrémente le compteur à chaque création
        Eleve.compteur_eleves += 1

alice = Eleve("Alice", 15)
bob = Eleve("Bob", 16)

# Chaque élève a son propre nom
print(alice.nom)  # Alice
print(bob.nom)    # Bob

# Mais tous partagent le même nom d'école
print(alice.nom_ecole)  # Python School
print(bob.nom_ecole)    # Python School

# Le compteur est aussi partagé
print(Eleve.compteur_eleves)  # 2

2.2 Quand utiliser quoi ?
Situation	Type d'attribut
Une caractéristique propre à chaque objet (nom, âge, couleur...)	Instance
Une valeur constante partagée par tous (pi, nom d'école...)	Classe
Un compteur d'instances	Classe
Une configuration globale	Classe
2.3 Le piège classique : modification via une instance
python

class Test:
    valeur = 10  # Attribut de classe

obj1 = Test()
obj2 = Test()

# Ceci ne modifie PAS l'attribut de classe !
obj1.valeur = 20

print(Test.valeur)  # 10 (pas changé)
print(obj1.valeur)  # 20 (c'est un NOUVEL attribut d'instance)
print(obj2.valeur)  # 10 (toujours l'attribut de classe)

# Pour modifier l'attribut de classe, utilisez la classe
Test.valeur = 30
print(obj2.valeur)  # 30 (maintenant c'est changé)

Pourquoi ? Quand on écrit obj1.valeur = 20, Python :

    Cherche d'abord s'il existe un attribut valeur dans l'instance obj1

    S'il n'existe pas, il en crée un NOUVEAU dans l'instance

    L'attribut de classe reste intact

C'est une source fréquente de bugs ! Pour modifier un attribut de classe, utilisez toujours NomClasse.attribut.
PARTIE 3 : MÉTHODES DE CLASSE ET MÉTHODES STATIQUES
3.1 Les 3 types de méthodes

En POO, on a trois types de méthodes, chacune ayant un rôle spécifique :
Type	Premier paramètre	Accès à l'instance	Accès à la classe	Quand l'utiliser ?
Instance	self	Oui	Oui (via self.__class__)	Action qui concerne UN objet spécifique
Classe	cls	Non	Oui	Action qui concerne LA CLASSE (constructeur alternatif)
Statique	rien	Non	Non	Fonction utilitaire liée logiquement à la classe
3.2 Méthodes d'instance (déjà vues)
python

class Personne:
    def __init__(self, nom):
        self.nom = nom
    
    def se_presenter(self):  # Méthode d'instance
        print(f"Je m'appelle {self.nom}")  # Utilise self

3.3 Méthodes de classe (@classmethod)

Une méthode de classe reçoit la classe (pas l'instance). Elle est utile pour :

    Créer des constructeurs alternatifs

    Modifier des attributs de classe

    Créer des "factory methods" (méthodes usines)

python

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    @classmethod
    def depuis_annee_naissance(cls, nom, annee_naissance):
        """Constructeur alternatif : crée une Personne à partir de l'année"""
        # cls = la classe Personne (pas une instance)
        age = 2026 - annee_naissance
        return cls(nom, age)  # Équivalent à Personne(nom, age)
    
    @classmethod
    def personne_anonyme(cls):
        """Constructeur alternatif : crée une personne sans nom"""
        return cls("Anonyme", 0)

# Utilisation
alice = Personne.depuis_annee_naissance("Alice", 2000)
# alice a automatiquement 26 ans sans qu'on ait à le calculer

anonyme = Personne.personne_anonyme()

Pourquoi utiliser une méthode de classe plutôt qu'une fonction normale ? Parce qu'elle est liée à la classe. Si un jour on renomme la classe ou qu'on crée une sous-classe, la méthode de classe s'adaptera automatiquement.
3.4 Méthodes statiques (@staticmethod)

Une méthode statique est une fonction ordinaire qui se trouve à l'intérieur d'une classe pour des raisons d'organisation.
python

class Maths:
    @staticmethod
    def est_pair(n):
        """Vérifie si un nombre est pair"""
        return n % 2 == 0
    
    @staticmethod
    def additionner(a, b):
        return a + b

# On n'a pas besoin de créer un objet Maths
print(Maths.est_pair(10))    # True
print(Maths.additionner(5, 3))  # 8

Différence entre méthode de classe et méthode statique :

    Méthode de classe : reçoit cls, peut accéder/modifier des attributs de classe

    Méthode statique : ne reçoit rien, est juste une fonction rangée dans la classe

PARTIE 4 : ENCAPSULATION ET PROPRIÉTÉS
4.1 Principe de l'encapsulation

L'encapsulation est le principe qui dit : cachez les détails internes d'un objet, exposez seulement ce qui est nécessaire.

Dans la vraie vie :

    Une voiture a un moteur complexe à l'intérieur. Tu n'as pas besoin de comprendre le moteur pour conduire.

    Tu utilises le volant, les pédales : ce sont des interfaces simples.

En programmation, on veut :

    Protéger les données internes contre des modifications invalides

    Cacher la complexité

4.2 Les conventions Python (pas de vrai privé)

Python n'a pas de mots-clés private ou protected comme Java. À la place, on utilise des conventions de nommage :
python

class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire      # Public : tout le monde peut y accéder
        self._solde = solde             # "Protégé" : convention = "ne touchez pas à ça"
        self.__mot_de_passe = "secret"  # "Privé" : le nom est caché (name mangling)

Convention	Signification	Devrait être utilisé par
nom	Public	Tout le monde
_nom	"Protégé"	La classe elle-même et ses sous-classes
__nom	"Privé"	La classe uniquement (le nom est transformé)

Le name mangling : __mot_de_passe devient _CompteBancaire__mot_de_passe. C'est possible d'y accéder, mais c'est intentionnellement difficile.
4.3 Les propriétés (@property) : le bonheur en Python

Au lieu d'écrire des getters et setters en Java :
java

// En Java
public class CompteBancaire {
    private double solde;
    
    public double getSolde() { return solde; }
    public void setSolde(double solde) { 
        if (solde >= 0) this.solde = solde;
    }
}

En Python, on utilise @property pour créer des attributs virtuels avec logique :
python

class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self._solde = solde  # Attribut "protégé"
    
    @property
    def solde(self):
        """Getter : appelé quand on lit compte.solde"""
        print(f"Demande du solde de {self.titulaire}")
        return self._solde
    
    @solde.setter
    def solde(self, valeur):
        """Setter : appelé quand on écrit compte.solde = X"""
        print(f"Tentative de modification du solde de {self.titulaire}")
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._solde = valeur

# Utilisation : tout se passe comme si solde était un attribut normal
compte = CompteBancaire("Alice", 1000)

# Lecture : appelle le getter
print(compte.solde)  # 1000

# Écriture : appelle le setter
compte.solde = 1500  # OK

# compte.solde = -100  # Déclenche une erreur !

Avantages des propriétés :

    Le code utilisateur n'a rien à changer : on lit/écrit comme un attribut normal

    On peut ajouter une logique de validation sans changer l'interface externe

    On peut rendre un attribut lecture seule (en omettant le setter)

4.4 Propriété calculée (lecture seule)
python

class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    @property
    def aire(self):
        """L'aire est calculée à partir de largeur et hauteur"""
        return self.largeur * self.hauteur
    
    @property
    def perimetre(self):
        """Le périmètre est calculé"""
        return 2 * (self.largeur + self.hauteur)

r = Rectangle(5, 3)
print(r.aire)        # 15 (appel sans parenthèses !)
print(r.perimetre)   # 16

# r.aire = 20  # ERREUR ! Pas de setter

Ici, aire et perimetre ne sont pas stockés. Ils sont calculés à la demande. C'est parfait pour des valeurs dérivées.
PARTIE 5 : HÉRITAGE
5.1 Principe de l'héritage

L'héritage est un mécanisme qui permet de créer une nouvelle classe à partir d'une classe existante.

La nouvelle classe (classe fille) hérite de tous les attributs et méthodes de la classe existante (classe mère).

Dans la vraie vie :

    Un "chien" est un type d'"animal"

    Un "camion" est un type de "véhicule"

    Un "étudiant" est un type de "personne"

La classe fille est spécialisation : elle ajoute ou modifie des comportements.
python

class Animal:
    """Classe mère (générale)"""
    def __init__(self, nom):
        self.nom = nom
    
    def manger(self):
        print(f"{self.nom} mange")
    
    def dormir(self):
        print(f"{self.nom} dort")

class Chien(Animal):  # Chien hérite de Animal
    """Classe fille (spécialisée)"""
    def aboyer(self):
        """Nouvelle méthode spécifique aux chiens"""
        print(f"{self.nom} aboie : Woof !")
    
    def manger(self):
        """REDÉFINITION (override) du comportement"""
        print(f"{self.nom} mange sa pâtée")

class Chat(Animal):
    """Classe fille (spécialisée)"""
    def miauler(self):
        print(f"{self.nom} miaule : Miaou !")
    
    def manger(self):
        print(f"{self.nom} mange ses croquettes")

# Utilisation
rex = Chien("Rex")
felix = Chat("Felix")

# Méthodes communes (héritées)
rex.dormir()   # Rex dort
felix.dormir()  # Felix dort

# Méthodes spécifiques
rex.aboyer()   # Rex aboie : Woof !
felix.miauler() # Felix miaule : Miaou !

# Même nom de méthode, comportement différent
rex.manger()   # Rex mange sa pâtée (redéfini)
felix.manger() # Felix mange ses croquettes (redéfini)

5.2 Le polymorphisme

Le polymorphisme est la capacité pour un même nom de méthode d'avoir des comportements différents selon l'objet qui l'exécute.
python

def nourrir_animal(animal):
    """Cette fonction accepte n'importe quel type d'animal"""
    animal.manger()  # Le comportement dépend du type réel

nourrir_animal(rex)    # Rex mange sa pâtée
nourrir_animal(felix)  # Felix mange ses croquettes
nourrir_animal(Animal("Bidule"))  # Bidule mange

Le polymorphisme permet d'écrire du code générique qui fonctionne avec n'importe quelle classe dérivée.
5.3 La fonction super()

super() permet d'appeler une méthode de la classe mère. Pourquoi ? Parce que quand on redéfinit une méthode, on veut souvent enrichir le comportement, pas le remplacer complètement.
python

class Animal:
    def __init__(self, nom, age=0):
        self.nom = nom
        self.age = age
    
    def afficher(self):
        print(f"Animal: {self.nom}, {self.age} ans")

class Chien(Animal):
    def __init__(self, nom, race, age=0):
        # super(). appel le constructeur de Animal
        super().__init__(nom, age)  # Évite de réécrire l'initialisation de nom et age
        self.race = race
    
    def afficher(self):
        super().afficher()  # Appelle la version de Animal
        print(f"Race: {self.race}")  # Puis ajoute l'info spécifique

rex = Chien("Rex", "Berger allemand", 5)
rex.afficher()
# Affiche :
# Animal: Rex, 5 ans
# Race: Berger allemand

Sans super() : tu devrais recopier tout le code de la classe mère. Avec super(), tu réutilises proprement le code existant.
5.4 Vérifier les types
python

# isinstance() : vérifie l'appartenance (y compris l'héritage)
print(isinstance(rex, Chien))    # True
print(isinstance(rex, Animal))   # True (car Chien hérite de Animal)

# type() : vérifie le type EXACT
print(type(rex) == Chien)    # True
print(type(rex) == Animal)   # False (rex est un Chien, pas un Animal direct)

# issubclass() : vérifie la relation de parenté entre CLASSES
print(issubclass(Chien, Animal))  # True
print(issubclass(Animal, Chien))  # False

5.5 Héritage multiple

Contrairement à Java (qui n'a que l'héritage simple), Python permet à une classe d'hériter de plusieurs classes mères.
python

class Volant:
    def voler(self):
        print("Je vole !")

class Nageur:
    def nager(self):
        print("Je nage !")

class Canard(Volant, Nageur):
    def crier(self):
        print("Coin coin !")

# Un canard peut voler ET nager !
donald = Canard()
donald.voler()   # Je vole !
donald.nager()   # Je nage !
donald.crier()   # Coin coin !

Quelle est l'utilité ? Cela permet de composer des comportements ("mixins"). Par exemple, un Canard a les capacités de voler ET de nager.

L'ordre d'héritage importe : en cas de conflit (deux classes mères ayant une méthode avec le même nom), c'est la première classe dans la liste qui l'emporte.
PARTIE 6 : MÉTHODES SPÉCIALES (MAGIC METHODS)
6.1 Principe

Les méthodes spéciales sont des méthodes qui commencent et finissent par __ (deux underscores). Elles sont appelées automatiquement par Python dans certaines situations.
python

# Par exemple, quand tu écris len(objet), Python appelle objet.__len__()
# Quand tu écris print(objet), Python appelle objet.__str__()
# Quand tu écris objet1 + objet2, Python appelle objet1.__add__(objet2)

Ces méthodes permettent de faire que nos objets se comportent comme des objets natifs de Python.
6.2 __str__ et __repr__
python

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def __str__(self):
        """Appelé par print() et str() - pour les utilisateurs finaux"""
        return f"Personne: {self.nom} ({self.age} ans)"
    
    def __repr__(self):
        """Appelé par repr() - pour les développeurs"""
        return f"Personne('{self.nom}', {self.age})"

alice = Personne("Alice", 25)
print(alice)           # Personne: Alice (25 ans)  (__str__)
print(repr(alice))     # Personne('Alice', 25)     (__repr__)

Différence :

    __str__ : doit être lisible par un humain. C'est ce qu'on voit avec print().

    __repr__ : doit être précise et si possible être du code qui recrée l'objet. C'est ce qu'on voit dans le débogueur.

6.3 __len__ et __getitem__ pour rendre un objet itérable
python

class Bibliotheque:
    def __init__(self):
        self.livres = []
    
    def ajouter(self, livre):
        self.livres.append(livre)
    
    def __len__(self):
        """Appelé par len()"""
        return len(self.livres)
    
    def __getitem__(self, index):
        """Appelé par [] et par les boucles"""
        return self.livres[index]

bib = Bibliotheque()
bib.ajouter("1984")
bib.ajouter("Dune")
bib.ajouter("Le Petit Prince")

print(len(bib))    # 3     (appelle __len__)
print(bib[0])      # 1984  (appelle __getitem__)

# La boucle for fonctionne grâce à __getitem__
for livre in bib:
    print(livre)

6.4 __add__ (surcharge d'opérateur)
python

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, autre):
        """Appelé par l'opérateur +"""
        return Vecteur(self.x + autre.x, self.y + autre.y)
    
    def __sub__(self, autre):
        """Appelé par l'opérateur -"""
        return Vecteur(self.x - autre.x, self.y - autre.y)
    
    def __mul__(self, scalaire):
        """Appelé par l'opérateur *"""
        return Vecteur(self.x * scalaire, self.y * scalaire)
    
    def __eq__(self, autre):
        """Appelé par l'opérateur =="""
        return self.x == autre.x and self.y == autre.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)

print(v1 + v2)   # (4, 6)  → appelle v1.__add__(v2)
print(v1 - v2)   # (-2, -2) → appelle v1.__sub__(v2)
print(v1 * 3)    # (3, 6)  → appelle v1.__mul__(3)
print(v1 == Vecteur(1, 2))  # True

6.5 Autres méthodes spéciales utiles
Méthode	Déclenchée par	Utilité
__eq__(self, other)	self == other	Égalité
__ne__(self, other)	self != other	Différence
__lt__(self, other)	self < other	Comparaison (tri)
__le__(self, other)	self <= other	Comparaison
__gt__(self, other)	self > other	Comparaison
__ge__(self, other)	self >= other	Comparaison
__contains__(self, item)	item in self	Test d'appartenance
__call__(self, *args)	self(*args)	Rendre l'objet appelable
__iter__(self)	for x in self	Rendre l'objet itérable