# Exercice R1 : Compter à rebours (le plus simple)

# Écris une fonction récursive compte_a_rebours(n) qui affiche les nombres de n jusqu'à 0.

# Exemple : compte_a_rebours(5) affiche :
# text

# 5
# 4
# 3
# 2
# 1
# 0

# Indices :

#     Cas de base : si n < 0, on arrête

#     Appel récursif : afficher n, puis rappeler la fonction avec n-1

# Exercice R2 : Compter de 0 à n

# Écris une fonction récursive compte_jusque(n) qui affiche les nombres de 0 jusqu'à n.

# Exemple : compte_jusque(5) affiche :
# text

# 0
# 1
# 2
# 3
# 4
# 5

# Indice : Plus difficile. Il faut une fonction qui prend deux paramètres (départ et arrivée). Ou une fonction qui affiche avant de s'appeler.
# Exercice R3 : Factorielle (révision)
# python

# def factorielle(n):
#     if n <= 1:
#         return 1
#     return n * factorielle(n-1)

# Teste avec factorielle(5) (doit afficher 120).
# Exercice R4 : Afficher les étapes de la factorielle

# Modifie la fonction factorielle pour qu'elle affiche le calcul étape par étape.

# Exemple pour factorielle(5) :
# text

# Appel factorielle(5)
# Appel factorielle(4)
# Appel factorielle(3)
# Appel factorielle(2)
# Appel factorielle(1)
# Retourne 1
# Retourne 2 × 1 = 2
# Retourne 3 × 2 = 6
# Retourne 4 × 6 = 24
# Retourne 5 × 24 = 120
# Résultat final : 120

# Exercice R5 : Somme des entiers de 0 à n (récursive)

# Écris une fonction récursive somme(n) qui calcule la somme des entiers de 0 à n.

# Exemple : somme(5) = 5+4+3+2+1+0 = 15

# Formule : somme(n) = n + somme(n-1) avec cas de base somme(0) = 0
# Exercice R6 : Puissance récursive

# Écris une fonction récursive puissance(x, n) qui calcule x^n (sans utiliser **).

# Exemple : puissance(2, 5) = 32

# Formule : x^n = x × x^(n-1) avec cas de base x^0 = 1
# Exercice R7 : Fibonacci récursif
# python

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# Teste avec fibonacci(7) (doit afficher 13).