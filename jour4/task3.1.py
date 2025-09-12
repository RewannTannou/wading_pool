message = input("please enter the message : ").lower()
key = int(input("please give the encryption key between 1 and 26 : "))
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
newMessage = ""
listeMessage = []
for element in message:
    listeMessage.append(element)
    placePhrase = listeMessage.index(element)
    if element in alphabet:
        # longueur = len(listeMessage)
        place = alphabet.index(element)
        nouvelleLettre = (
            place + key
        ) % 26  # remplacer la lettre par la meme +key dans la l'alphabet
        newMessage += alphabet[nouvelleLettre]
    else:
        newMessage += element

print(newMessage)
