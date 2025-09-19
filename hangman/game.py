import os
from random import choice
from unidecode import unidecode


class Game:
    def __init__(self, mots_file):
        self.mots_file = mots_file
        self.max_erreurs = 6
        self.resetVar()

    def load_word(self):
        with open(self.mots_file, "r", encoding="utf8") as f:
            lines = f.readlines()
        return unidecode(choice(lines).strip())

    def resetVar(self):
        self.mot = self.load_word()
        self.correct_guessed = []
        self.wrong_guessed = []
        self.erreurs = 0
        self.message = ""
        self.game_over = False

    def guess(self, lettre):
        if self.game_over:
            return
        lettre = lettre.lower()
        if lettre in self.correct_guessed or lettre in self.wrong_guessed:
            self.message = "Vous avez déjà essayé cette lettre."
        elif lettre in self.mot:
            self.correct_guessed.append(lettre)
            self.message = "Bien joué !"
        else:
            self.wrong_guessed.append(lettre)
            self.erreurs += 1
            self.message = (
                f"Raté ! Il vous reste {self.max_erreurs - self.erreurs} essais."
            )

        if self.erreurs >= self.max_erreurs or all(
            l in self.correct_guessed for l in self.mot
        ):
            self.game_over = True

    def get_word(self):
        return " ".join([l if l in self.correct_guessed else "_" for l in self.mot])
