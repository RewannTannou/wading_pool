from random import choice  # permet de choisir un élément au hasard dans une liste
from english_words import (
    get_english_words_set,
)  # permet de récupérer une liste de mots anglais

# étapes du pendu en ASCII art (chaque dessin représente une erreur supplémentaire)
stages = [
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
    # récupère un ensemble de mots anglais (ici dictionnaire web2)
    web2lowerset = get_english_words_set(["web2"], lower=True)
    # transforme l’ensemble en liste puis choisit un mot au hasard
    return choice(list(web2lowerset))


def display_word(word, guessed):
    # retourne le mot avec les lettres trouvées, et _ pour les lettres manquantes
    return " ".join([letter if letter in guessed else "_" for letter in word])


def pendu():
    word = get_random_word()  # mot à deviner
    correct_guessed = set()  # lettres trouvées correctement
    wrong_guessed = set()  # lettres fausses
    max_attempts = len(stages) - 1  # nombre maximum d’erreurs autorisées

    print("Bienvenue dans le jeu du Pendu !")

    # boucle principale : continue tant qu’il reste des essais et que le mot n’est pas trouvé
    while len(wrong_guessed) < max_attempts and set(word) != correct_guessed:
        print(stages[len(wrong_guessed)])  # affiche l’état actuel du pendu
        print(
            display_word(word, correct_guessed)
        )  # affiche le mot avec les lettres découvertes
        print(
            f"Lettres déjà proposées : {' '.join(sorted(correct_guessed | wrong_guessed))}"
        )

        # demande une lettre à l’utilisateur
        guess = input("Entrez une lettre : ").lower()

        # vérifie que l’entrée est une seule lettre alphabétique
        if len(guess) != 1 or not guess.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue

        # vérifie si la lettre a déjà été proposée
        if guess in correct_guessed or guess in wrong_guessed:
            print("Vous avez déjà essayé cette lettre.")
            continue

        # si la lettre est dans le mot → ajout aux lettres trouvées
        if guess in word:
            correct_guessed.add(guess)
            print("Bien joué !")
        else:
            # sinon → ajout aux mauvaises lettres + perte d’un essai
            wrong_guessed.add(guess)
            print(f"Raté ! Il vous reste {max_attempts - len(wrong_guessed)} essais.")

    # affichage final après la boucle
    print(stages[len(wrong_guessed)])  # état final du pendu
    if set(word) == correct_guessed:
        print(f"Bravo, vous avez trouvé le mot : {word}")  # victoire
    else:
        print(f"Looser 🤪! Le mot était : {word}")  # défaite


pendu()  # lance le jeu
