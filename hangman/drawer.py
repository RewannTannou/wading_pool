import pygame

BLANC = (255, 255, 255)
ROUGE = (200, 50, 50)
VERT = (50, 200, 50)
BLEU = (0, 0, 255)


class Drawer:
    def __init__(self, fenetre, largeur, hauteur, font_main, font_small, font_image):
        self.fenetre = fenetre
        self.largeur = largeur
        self.hauteur = hauteur
        self.font_main = font_main
        self.font_small = font_small
        self.font_image = font_image
        self.fond = pygame.image.load(font_image)
        self.fond = pygame.transform.scale(self.fond, (largeur, hauteur))

    def draw_Background(self):
        self.fenetre.blit(self.fond, (0, 0))

    def draw_hangman(self, erreurs):
        # Poteau
        pygame.draw.line(self.fenetre, BLANC, (50, 400), (50, 150), 5)
        pygame.draw.line(self.fenetre, BLANC, (50, 150), (200, 150), 5)
        pygame.draw.line(self.fenetre, BLANC, (200, 150), (200, 200), 5)

        etapes = [
            lambda: pygame.draw.circle(self.fenetre, BLANC, (200, 230), 30, 3),
            lambda: pygame.draw.line(self.fenetre, BLANC, (200, 260), (200, 330), 3),
            lambda: pygame.draw.line(self.fenetre, BLANC, (200, 260), (160, 290), 3),
            lambda: pygame.draw.line(self.fenetre, BLANC, (200, 260), (240, 290), 3),
            lambda: pygame.draw.line(self.fenetre, BLANC, (200, 330), (170, 380), 3),
            lambda: pygame.draw.line(self.fenetre, BLANC, (200, 330), (230, 380), 3),
        ]
        for i in range(erreurs):
            etapes[i]()

    def draw_buttons(self, bouton_quitter, bouton_relancer):
        # quitter
        pygame.draw.rect(self.fenetre, ROUGE, bouton_quitter)
        texte = self.font_main.render("Quitter", True, BLANC)
        self.fenetre.blit(texte, (bouton_quitter.x + 20, bouton_quitter.y + 15))
        # relancer
        pygame.draw.rect(self.fenetre, VERT, bouton_relancer)
        texte = self.font_main.render("Relancer", True, BLANC)
        self.fenetre.blit(texte, (bouton_relancer.x + 20, bouton_relancer.y + 15))

    def draw_letters_used(self, zone_lettres, correct_guessed, wrong_guessed):
        surface_lettres = pygame.Surface(
            (zone_lettres.width, zone_lettres.height), pygame.SRCALPHA
        )
        surface_lettres.fill((0, 0, 0, 120))
        pygame.draw.rect(surface_lettres, BLANC, surface_lettres.get_rect(), 2)
        self.fenetre.blit(surface_lettres, (zone_lettres.x, zone_lettres.y))

        # Afficher lettres utilisées
        lettre_y = zone_lettres.y + 10
        for lettre in correct_guessed:
            lettre_surf = self.font_small.render(lettre.upper(), True, VERT)
            self.fenetre.blit(lettre_surf, (zone_lettres.x + 10, lettre_y))
            lettre_y += 30
        for lettre in wrong_guessed:
            lettre_surf = self.font_small.render(lettre.upper(), True, ROUGE)
            self.fenetre.blit(lettre_surf, (zone_lettres.x + 10, lettre_y))
            lettre_y += 30
