# Exercice 1 : Classe Personnage

# Crée une classe Personnage avec :

#     Attributs : nom, points_de_vie, force

#     Méthode attaquer() qui affiche "X attaque et inflige Y dégâts !"

# class Personnage :
#     def __init__(self, nom, point_de_vie, force):
#         self.nom = nom
#         self.point_de_vie = point_de_vie
#         self.force = force
#     def attaquer(self):
#         print(f"{self.nom} attaque et inflige {self.force} degats ")
# guerrier = Personnage("koko", 100, 15)
# guerrier.attaquer()

# Exercice 2 : Classe CompteBancaire

# Crée une classe CompteBancaire avec :

#     Attributs : titulaire, solde (initialisé à 0)

#     Méthodes : deposer(montant), retirer(montant), afficher_solde()

# class CompteBanquaire:

#     def __init__(self, titulaire, solde=0):
#         self.titulaire =titulaire
#         self.solde = solde
 
#     def deposer(self, montant):
#         self.solde += montant

#     def retirer(self, montant):
#         self.solde -= montant
 
#     def aff_solde(self):
#         print(f"{self.titulaire} possede un solde de  {self.solde} ")

# compte = CompteBanquaire("alice")
# compte.deposer(100)
# compte.retirer(30)
# compte.aff_solde()

# xercice 3 : Classe Livre

# Crée une classe Livre avec :

#     Attributs : titre, auteur, annee

#     Méthode description() qui retourne une phrase : "« Titre » de Auteur (année)"

# class Livre:
    
#     def __init__(self, titre, auteur, annee):
#         self.titre = titre
#         self.auteur = auteur
#         self.annee = annee
    
#     def description(self):
#         return f"le titre est {self.titre} ecrit par {self.auteur} en {self.annee}"

# livre = Livre("1984", "George Orwell", 1949)
# print(livre.description())
        
# -------------------------------------------------------------------------------------------------------------
# Exercice 5 : Classe Rectangle

# Crée une classe Rectangle avec :

#     Attributs : longueur, largeur

#     Méthodes : aire() (longueur × largeur), perimetre() (2 × (L + l))

# class Rectangle:
#     def __init__(self, longueur, largeur):
#         self.longueur = longueur
#         self.largeur = largeur
#     def aire(self):
#         return self.largeur*self.longueur
#     def perimetre(self):
#         return 2*(self.largeur+self.longueur)
    
# rect = Rectangle(5,3)
# print(rect.aire())
# print(rect.perimetre())
        

# -------------------------------------------------------------------------------------------------------------
# Exercice 7 : Classe Élève (avec listes)

# Crée une classe Eleve avec :

#     Attributs : nom, notes (liste vide par défaut)

#     Méthodes : ajouter_note(note), moyenne()

# class Eleve:
#     def __init__(self, nom, notes=None):
#         self.nom= nom
#         if notes is None:
#             self.notes = []
#         else:
#             self.notes = notes
#     def ajouter_note(self, note):
#         self.notes.append(note)
#     def moyenne(self):
#         somme = 0
#         for n in self.notes:
#             somme += n
#         return somme/len(self.notes)
# eleve=Eleve("Alice")
# eleve.ajouter_note(15)
# eleve.ajouter_note(12)
# print(eleve.moyenne())


# -------------------------------------------------------------------------------------------------------------
# Exercice 8 : Classe Lampe (avec propriété @property)

# Crée une classe Lampe avec :

#     Attribut privé : _allume (booléen, False par défaut)

#     Méthodes : allumer(), eteindre()

#     Propriété est_allume qui retourne l'état (lecture seule)

# class Lampe:
#     def __init__(self, est_allume = False):
#         self._est_allume = est_allume
#     def allumer(self):
#         self._est_allume = True
#     def eteindre(self):
#         self._est_allume = False
#     @property
#     def est_allume(self):
#         return self._est_allume
# # Exemple d'utilisation
# lampe = Lampe()
# lampe.allumer()
# print(lampe.est_allume)  # True
# lampe.eteindre()
# print(lampe.est_allume)  # False
# -------------------------------------------------------------------------------------------------------------
# Exercice 9 : Héritage simple - Animal

# Crée une classe Animal avec :

#     Attributs : nom, age

#     Méthode manger() qui affiche "X mange"

# Puis une classe Chat qui hérite de Animal avec :

#     Méthode miauler() qui affiche "Miaou !"

# class Animal:
#     def __init__(self, nom, age):
#         self.age = age
#         self.nom = nom
#     def manger(self):
#         print ( f"{self.nom} mange")
# class Chat(Animal):
#     def miauler(self):
#         print("Miaou")
# # Exemple d'utilisation
# chat = Chat("Felix", 3)
# chat.manger()   # "Felix mange"
# chat.miauler()  # "Miaou !"
# -------------------------------------------------------------------------------------------------------------
# Exercice 10 : Getter/Setter avec validation

# Crée une classe Temperature avec :

#     Attribut privé _celsius

#     Propriété celsius (getter et setter)

#     Setter qui refuse les températures en dessous de -273.15 ("Température impossible")

# class Temperature:
#     def __init__(self, celsius=0):
#         self._celsius = celsius
#     @property
#     def celsius(self):
#         return self._celsius
#     @celsius.setter
#     def celsius(self, valeur):
#         if valeur< -273.15:
#             print("temperature impossible")
#         else:
#             self._celsius = valeur
# # Exemple d'utilisation
# temp = Temperature()
# temp.celsius = 25
# print(temp.celsius)  # 25
# # temp.celsius = -300  # Affiche "Température impossible"
# # -------------------------------------------------------------------------------------------------------------
# Exercice 11 : Héritage - Véhicules (validation)

# Crée une classe Vehicule avec :

#     Attributs : marque, modele, annee

#     Méthode afficher_infos() qui affiche "Marque, Modèle (année)"

# Puis une classe Voiture qui hérite de Vehicule avec :

#     Attribut supplémentaire : nombre_portes

#     Redéfinition de afficher_infos() pour ajouter le nombre de portes

# class Vehicule:
#     def __init__(self, marque, modele, annee):
#         self.marque= marque
#         self.modele= modele
#         self.annee = annee
#     def afficher_infos(self):
#         print(f"{self.marque} {self.modele} ({self.annee})", end="")
# class Voiture(Vehicule):
#     def __init__(self,marque, modele,annee, nombre_portes):
#         super().__init__(marque, modele, annee)
#         self.nombre_portes= nombre_portes
#     def afficher_infos(self):
#          super().afficher_infos() 
#          print(f" - {self.nombre_portes} portes")
# # Exemple d'utilisation
# v = Voiture("Renault", "Clio", 2020, 5)
# v.afficher_infos()  # "Renault, Clio (2020) - 5 portes"
# -------------------------------------------------------------------------------------------------------------
# Exercice 12 : Héritage - Compte bancaire (avec super())

# Crée une classe Compte avec :

#     Attributs : titulaire, solde

#     Méthode deposer(montant) et retirer(montant)

# Puis une classe CompteEpargne qui hérite de Compte avec :

#     Attribut supplémentaire : taux_interet

#     Méthode appliquer_interets() qui augmente le solde en fonction du taux

# Utilise super().__init__() dans le constructeur.

# class Compte:
#     def __init__(self, titulaire, solde):
#         self.titulaire = titulaire
#         self.solde = solde
#     def deposer(self, montant):
#         self.solde += montant
#     def retirer(self, montant):
#         self.solde -= montant

# class CompteEpargne(Compte):
#     def __init__(self, titulaire, solde, taux_interet):
#         super().__init__(titulaire, solde)
#         self.taux_interet = taux_interet
#     def appliquer_interet(self):
#         self.solde += self.solde*self.taux_interet
 
#  # Exemple d'utilisation
# ce = CompteEpargne("Alice", 1000, 0.02)
# ce.appliquer_interet()
# print(ce.solde)  # 1020.0   


# # -------------------------------------------------------------------------------------------------------------
# Exercice 14 : Méthodes de classe (constructeur alternatif)

# Crée une classe Personne avec :

#     Attributs : nom, age

#     Constructeur classique __init__(nom, age)

#     Méthode de classe depuis_annee_naissance(nom, annee_naissance) qui calcule l'âge et crée une instance

# class Personne:
#     def __innit__(self, nom, age):
#         self.nom = nom
#         self.age = age
#     @classmethod
#     def depuis_annee_naisssance(cls, nom, annee_naissance):
#         age = 2026-annee_naissance
#         return(cls(nom,age))
# # -------------------------------------------------------------------------------------------------------------
# Exercice 15 : Classes abstraites

# Crée une classe abstraite Forme avec :

#     Méthode abstraite aire()

#     Méthode abstraite perimetre()

# Puis deux classes concrètes Rectangle et Cercle qui implémentent ces méthodes.
from abc import ABC, abstractmethod
class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass
    @abstractmethod
    def perimetre(self):
        pass
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def aire(self):
        return self.longueur*self.largeur
    def perimetre(self):
        return 2 * (self.longueur+self.largeur)
# Exemple d'utilisation
rect = Rectangle(5, 3)

print(rect.aire())      # 15
print(rect.perimetre()) # ~25.13  
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------






# -------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------
