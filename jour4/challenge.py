texte = input("veuillez entrer un texte : ")
nombre = int(input("Veuillez entrer un nombre : "))
listOfVowel = ["a", "e", "i", "o", "u", "y"]
lettreDeLaPhrase = []
if nombre == 0:
    quit
else:
    for element in texte:
        lettreDeLaPhrase.append(element)
        if lettreDeLaPhrase.__contains__(listOfVowel) == False:
            print(nombre)
        if nombre >= 42:
            print(nombre)
            break
        else:
            print(texte)
            break
