from random import choice
from english_words import (
    get_english_words_set,
)


# étapes du pendu
etapes = [
    """
     ------
     |    |
     |
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    _|_
    """,
]


def get_random_word():

    web2lowerset = get_english_words_set(["web2"], lower=True)

    return choice(list(web2lowerset))


def display_word(word, guessed):
    # retourne le mot avec les lettres trouvées, et _ pour les lettres manquantes
    return " ".join([letter if letter in guessed else "_" for letter in word])


def pendu():
    word = get_random_word()
    correct_guessed = set()
    wrong_guessed = set()
    max_attempts = len(etapes) - 1

    print("Bienvenue dans le jeu du Pendu !")
    print("Le mot a trouvé à", len(word), "lettres")
    # continue tant qu’il reste des essais et que le mot n’est pas trouvé
    while len(wrong_guessed) < max_attempts and set(word) != correct_guessed:
        print(etapes[len(wrong_guessed)])  # affiche l’état actuel du pendu
        print(
            display_word(word, correct_guessed)
        )  # affiche le mot avec les lettres découvertes
        print(
            f"Lettres déjà proposées : {' '.join(sorted(correct_guessed | wrong_guessed))}"
        )

        # demande une lettre à l’utilisateur
        guess = input("Entrez une lettre : ").lower()

        # vérifie que l’entrée est une seule lettre
        if len(guess) != 1 or not guess.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue

        # vérifie si la lettre a déjà été proposée
        if guess in correct_guessed or guess in wrong_guessed:
            print("Vous avez déjà essayé cette lettre.")
            continue

        if guess in word:
            correct_guessed.add(guess)
            print("Bien joué !")
        else:
            wrong_guessed.add(guess)
            print(f"Raté ! Il vous reste {max_attempts - len(wrong_guessed)} essais.")

    # affichage final
    print(etapes[len(wrong_guessed)])
    if set(word) == correct_guessed:
        print(f"Bravo, vous avez trouvé le mot : {word}")
    else:
        print(f"Looser 🤪! Le mot était : {word}")


pendu()
