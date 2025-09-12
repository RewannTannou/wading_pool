# variable avec l'input
nombre = int(input("give me a number : "))
# pour i entre 2 et le nombre donné divisé par deux tout en restant sur un int +1
for i in range(2, nombre // 2 + 1):
    # créer un liste vide
    listeMultiple = []
    # pour chaque d dans l'ordre decroissant
    for d in reversed(range(nombre)):
        # si le reste de d / i est égal a 0 et d est différent de 0
        if d % i == 0 and d != 0:
            # alors on ajoute d a liste
            listeMultiple.append(d)
    # afficher la liste
    print(listeMultiple)
