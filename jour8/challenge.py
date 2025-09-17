from turtle import *

ListCouleur = [
    "red",
    "blue",
    "green",
    "magenta",
    "cyan",
    "orange",
    "purple",
    "pink",
    "yellow",
    "brown",
    "gray",
]

speed(0)  # vitesse max (même si on coupe l'anim)
tracer(False)  # désactive l'animation

# for steps in range(300, 0, -1):

#     for couleur in ListCouleur:

#         forward(steps)
#         left(100)
#         color(couleur)
from turtle import *


speed(0)  # vitesse max (même si on coupe l'anim)
tracer(False)

import turtle

# Configuration de la fenêtre
t = turtle.Turtle()
t.color("purple")

# Dessin de la rosace
for i in range(41):
    t.left(600)
    t.circle(100, 100)
    t.left(600)
    t.left(5)


update()  # affiche tout d’un coup
done()


# trouver sur internet laisser pour le test
# import turtle
# import math

# kalam = turtle.Turtle()
# kalam.speed(500)

# window = turtle.Screen()
# window.bgcolor("#000000")
# kalam.color("yellow")

# ankur = 20

# kalam.left(90)
# kalam.penup()
# kalam.goto(-7 * ankur, 0)
# kalam.pendown()
# kalam.begin_fill()

# for a in range(-7 * ankur, -3 * ankur, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = 1.5 * math.sqrt(
#         (-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))
#     ) * (1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
#         4.5
#         + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5))
#         - 2.75 * (math.fabs(x - 0.75) + math.fabs(x + 0.75))
#     ) * (
#         1 + math.fabs(1 - rel) / (1 - rel)
#     )
#     kalam.goto(a, y * ankur)

# for a in range(-3 * ankur, -1 * ankur - 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (lenght
#         2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)
#     ) * math.sqrt(math.fabs(rel - 1) / (rel - 1))
#     kalam.goto(a, y * ankur)

# kalam.goto(-1 * ankur, 3 * ankur)
# kalam.goto(int(-0.5 * ankur), int(2.2 * ankur))
# kalam.goto(int(0.5 * ankur), int(2.2 * ankur))
# kalam.goto(1 * ankur, 3 * ankur)
# print("Batman Logo with Python Turtle")
# for a in range(1 * ankur + 1, 3 * ankur + 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (
#         2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)
#     ) * math.sqrt(math.fabs(rel - 1) / (rel - 1))
#     kalam.goto(a, y * ankur)

# for a in range(3 * ankur + 1, 7 * ankur + 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = 1.5 * math.sqrt(
#         (-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))
#     ) * (1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
#         4.5
#         + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5))
#         - 2.75 * (math.fabs(x - 0.75) + math.fabs(x + 0.75))
#     ) * (
#         1 + math.fabs(1 - rel) / (1 - rel)
#     )
#     kalam.goto(a, y * ankur)

# for a in range(7 * ankur, 4 * ankur, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
#     kalam.goto(a, y * ankur)

# for a in range(4 * ankur, -4 * ankur, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (
#         math.fabs(x / 2)
#         - 0.0913722 * x**2
#         - 3
#         + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
#     )
#     kalam.goto(a, y * ankur)

# for a in range(-4 * ankur - 1, -7 * ankur - 1, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
#     kalam.goto(a, y * ankur)

# kalam.end_fill()

# kalam.penup()
# kalam.goto(300, 300)
# turtle.done()
