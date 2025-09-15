import re
import unicodedata


# region clear chaine
def nettoyer_chaine(texte: str) -> str:
    # 1. Supprimer accents
    texte = unicodedata.normalize(
        "NFD", texte
    )  # décompose les lettres accentuées en lettre + accent séparé.
    texte = "".join(
        c for c in texte if unicodedata.category(c) != "Mn"
    )  # enlève tous les accents, ne gardant que la lettre de base.

    texte = re.sub(r"[^a-zA-Z0-9]", "", texte)  # Supprimer tout sauf lettres/chiffres
    return texte.lower()


# endregion


def isPalindrome(word: str):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return isPalindrome(word[1:-1])


def palindromeFunc():
    chars = input("enter a word : ")
    if isPalindrome(chars):
        print("this is a palindrome")
    else:
        print("this is not a palindrome")


palindromeFunc()
