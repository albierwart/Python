pour demander une donnee a l utilisateur --> input("blalbalba") ⚠️ return un str(string)

liste append()

    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6]

# append() ajoute la liste ENTIÈRE comme un seul élément
    liste2.append(liste1)
    print(liste2)  # [4, 5, 6, [1, 2, 3]]  ← Liste imbriquée !

# extend() ajoute chaque élément un par un
    liste2.extend(liste1)
    print(liste2)  # [4, 5, 6, 1, 2, 3]  ← Liste plate
    extend() ou += = ajoute les éléments un par un

    append() = ajoute la liste entière comme un seul élément

    + = crée une nouvelle liste sans modifier les originales
    
    append() → ajoute 1 élément (même si cet élément est une liste, un tuple, etc.)

suivant