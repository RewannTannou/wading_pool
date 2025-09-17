import turtle

t = turtle.Turtle()
listCouleur = ["red", "blue", "green", "yellow"]
for _ in range(4):
    for couleur in listCouleur:
        t.color(couleur)

        t.forward(90)
        t.left(90)
