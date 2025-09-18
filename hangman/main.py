import pygame
from game import Game
from drawer import Drawer
from score_gestion import ScoreManager

pygame.init()
clock = pygame.time.Clock()
running = True

largeur, hauteur = 850, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")

font_main = pygame.font.Font(None, 40)
font_small = pygame.font.Font(None, 30)

bouton_quitter = pygame.Rect(150, 500, 150, 60)
bouton_relancer = pygame.Rect(350, 500, 150, 60)
zone_lettres = pygame.Rect(700, 100, 200, 400)

# Initialisation classes
game = Game(r"C:\Users\tanno\Documents\wadingPool\hangman\mots_pendu.txt")
Drawer = Drawer(fenetre, largeur, hauteur, font_main, font_small, "hangman/arbre.jpg")
score_manager = ScoreManager("best_scores.txt")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_quitter.collidepoint(event.pos):
                running = False
            if bouton_relancer.collidepoint(event.pos):
                game.resetVar()

        if event.type == pygame.KEYDOWN and not game.game_over:
            lettre = event.unicode
            if lettre.isalpha() and len(lettre) == 1:
                game.guess(lettre)

    # Dessiner tout
    Drawer.draw_Background()
    Drawer.draw_hangman(game.erreurs)

    mot_affiche = font_main.render(game.get_word(), True, (255, 255, 255))
    fenetre.blit(mot_affiche, (150, 450))

    Drawer.draw_buttons(bouton_quitter, bouton_relancer)
    Drawer.draw_letters_used(zone_lettres, game.correct_guessed, game.wrong_guessed)

    # Messages fin de partie
    if game.game_over:
        if game.erreurs >= game.max_erreurs:
            msg = font_small.render(
                f"Perdu ! Le mot était : {game.mot}", True, (200, 50, 50)
            )
            fenetre.blit(msg, (150, 50))
        else:
            attempts = len(game.correct_guessed) + len(game.wrong_guessed)
            best = score_manager.get_best_score()
            if best is None or attempts < best:
                score_manager.save_score(game.mot, attempts)
                msg = font_small.render(
                    f"Meilleur score ! {attempts} essais", True, (0, 0, 250)
                )
            else:
                msg = font_small.render(
                    f"Tu as trouvé {game.mot} en {attempts} essais. Record : {best}",
                    True,
                    (0, 0, 250),
                )
            fenetre.blit(msg, (150, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
