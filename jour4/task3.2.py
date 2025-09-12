message = input("please enter the message : ").lower()
# region alphabet
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
# endregion
# region key
key = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
]
# endregion
newMessage = ""
listeMessage = []
for i in key:
    for element in message:
        listeMessage.append(element)
        placePhrase = listeMessage.index(element)
        if element in alphabet:
            # longueur = len(listeMessage)
            place = alphabet.index(element)
            nouvelleLettre = (
                place - i
            ) % 26  # remplacer la lettre par la meme +key dans la l'alphabet
            newMessage += alphabet[nouvelleLettre]
        else:
            newMessage += element

print(newMessage)
