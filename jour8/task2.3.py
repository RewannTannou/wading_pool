from turtle import *


def buildPoligon(nb: int, length: int):
    cote = 360 / nb
    for i in range(nb):
        forward(length)
        left(cote)


buildPoligon(3, 20)
# from turtle import *


# def buildPolygon(nb: int, length: int):
#     circle(length, steps=nb)  # steps = nombre de côtés


# buildPolygon(3, 100)  # polygone de 10 côtés inscrit dans un cercle
# done()
