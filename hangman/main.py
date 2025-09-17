import pygame
from random import choice
from english_words import get_english_words_set

pygame.init()
clock = pygame.time.Clock()
running = True
largeur, hauteur = 480, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")

# Charger le fond
fond = pygame.image.load("hangman/f1c38e675e39e7c32d27c915546c5fc6.jpg")
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Couleurs
BLANC = (255, 255, 255)
ROUGE = (200, 50, 50)
NOIR = (0, 0, 0)
VERT = (50, 200, 50)

# Police
police = pygame.font.Font(None, 40)
petite_police = pygame.font.Font(None, 30)

# Bouton quitter
bouton_rect = pygame.Rect(150, 500, 150, 60)


web2lowerset = get_english_words_set(["web2"], lower=True)
mot = choice(list(web2lowerset))
correct_guessed = set()
wrong_guessed = set()
max_erreurs = 6
erreurs = 0
message = ""


def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])


def dessiner_pendu(erreurs):
    # Poteau
    pygame.draw.line(fenetre, BLANC, (50, 400), (50, 100), 5)
    pygame.draw.line(fenetre, BLANC, (50, 100), (200, 100), 5)
    pygame.draw.line(fenetre, BLANC, (200, 100), (200, 150), 5)

    if erreurs > 0:
        pygame.draw.circle(fenetre, BLANC, (200, 180), 30, 3)
    if erreurs > 1:
        pygame.draw.line(fenetre, BLANC, (200, 210), (200, 300), 3)
    if erreurs > 2:
        pygame.draw.line(fenetre, BLANC, (200, 220), (160, 260), 3)
    if erreurs > 3:
        pygame.draw.line(fenetre, BLANC, (200, 220), (240, 260), 3)
    if erreurs > 4:
        pygame.draw.line(fenetre, BLANC, (200, 300), (170, 350), 3)
    if erreurs > 5:
        pygame.draw.line(fenetre, BLANC, (200, 300), (230, 350), 3)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Vérifier si on clique sur le bouton
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_rect.collidepoint(event.pos):
                running = False

        # Gestion des lettres tapées
        if event.type == pygame.KEYDOWN:
            lettre = event.unicode.lower()
            if lettre.isalpha() and len(lettre) == 1:
                if lettre in correct_guessed or lettre in wrong_guessed:
                    message = "Vous avez déjà essayé cette lettre."
                elif lettre in mot:
                    correct_guessed.add(lettre)
                    message = "Bien joué !"
                else:
                    wrong_guessed.add(lettre)
                    erreurs += 1
                    message = f"Raté ! Il vous reste {max_erreurs - erreurs} essais."

    # Afficher le fond
    fenetre.blit(fond, (0, 0))

    # Dessiner le pendu
    dessiner_pendu(erreurs)

    # Afficher le mot
    mot_affiche = police.render(display_word(mot, correct_guessed), True, BLANC)
    fenetre.blit(mot_affiche, (50, 450))

    # Afficher message
    message_surf = petite_police.render(message, True, ROUGE)
    fenetre.blit(message_surf, (50, 30))

    # Dessiner le bouton
    pygame.draw.rect(fenetre, ROUGE, bouton_rect)
    texte = police.render("Quitter", True, BLANC)
    fenetre.blit(texte, (bouton_rect.x + 20, bouton_rect.y + 15))

    # Vérifier fin de partie
    if set(mot) == correct_guessed:
        fin_surf = police.render(f"Bravo ! Le mot était : {mot}", True, VERT)
        fenetre.blit(fin_surf, (50, 50))
    elif erreurs >= max_erreurs:
        fin_surf = police.render(f"Perdu ! Le mot était : {mot}", True, NOIR)
        fenetre.blit(fin_surf, (30, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
