first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [*zip(first_names, last_names[::-1])]
print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])
# permet de creer une liste ou les element[0] des deux listes seront l'element[0] de la nouvelle liste
