string format

Code	Signification	Exemple	Résultat
:d	Entier décimal	{42:d}	42
:f	Flottant	{3.14:f}	3.140000
:.2f	Flottant à 2 décimales	{3.14159:.2f}	3.14
:e	Notation scientifique	{1234:e}	1.234000e+03
:%	Pourcentage	{0.75:%}	75.000000%
:.1%	Pourcentage à 1 décimale	{0.7523:.1%}	75.2%

centrer les chiffres 

    nombre = 125

    print("Alignement à droite (défaut) :")
    print(f"|{nombre:8d}|")      # |     125|

    print("\nAlignement à gauche :")
    print(f"|{nombre:<8d}|")     # |125     |

    print("\nCentrage :")
    print(f"|{nombre:^8d}|")     # |  125   |

Avec des nombres décimaux
    valeur = 125.45
    
    print(f"|{valeur:10.2f}|")      # |    125.45| (droite)
    print(f"|{valeur:<10.2f}|")     # |125.45    | (gauche)
    print(f"|{valeur:^10.2f}|")     # |  125.45  | (centre)

Avec du texte (chaînes de caractères)
    texte = "Python"
    
    print(f"|{texte:10s}|")        # |Python    | (gauche par défaut pour str)
    print(f"|{texte:<10s}|")       # |Python    | (gauche)
    print(f"|{texte:>10s}|")       # |    Python| (droite)
    print(f"|{texte:^10s}|")       # |  Python  | (centre)

Combinaison avec des caractères de remplissage
    nombre = 125

    # Remplir avec des zéros
    print(f"{nombre:08d}")        # 00000125

    # Remplir avec des étoiles (alignement droite)
    print(f"{nombre:*>8d}")       # *****125

    # Remplir avec des tirets (alignement gauche)
    print(f"{nombre:-<8d}")       # 125-----

    # Remplir avec des points (centrage)
    print(f"{nombre:.^8d}")       # ..125...
    
print("-" * 30) --> -------------------------

Afficher des données alignées
    produits = [
    ("Clavier", 45.99),
    ("Souris", 12.50),
    ("Écran 27 pouces", 199.90),
    ("Casque audio", 79.99)
    ]

    print(f"{'Produit':<20} {'Prix':>10}")
    print("-" * 30)
    for nom, prix in produits:
    print(f"{nom:<20} {prix:>10.2f} €")
     
    Résultat :
        Produit                   Prix
    ------------------------------
    Clavier                  45.99 €
    Souris                   12.50 €
    Écran 27 pouces         199.90 €
    Casque audio             79.99 €