
from pygame import key, Rect, Surface, Vector2, draw, Rect
from pygame.constants import K_DOWN, K_UP
from objects.ball import Ball

# Définition de la classe Paddle
class Paddle():

    # Constructeur de la classe
    def __init__(self, ball: Ball = None, is_player=True, x = 0):
        # Position de la raquette
        self.rect = Rect(0, 0, 5, 100)
        self.rect.x = x
        # La raquette est controlée par le joueur ? O/N
        self.is_player = is_player
        # Quelle est la balle du jeu (pour l'IA)
        self.ball = ball
        # Vitesse de déplacement de la raquette
        self.speed = 2

    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        self.screen = screen

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self):
        # Il existe une fonction par type de joueur, manuel ou IA
        if (self.is_player):
            self.manual_control()
        else:
            self.automatic_control()

        # Maintenant que les coordonées ont changés, on dessine la raquette
        draw.rect(self.screen, (255, 255, 255), self.rect)

    def manual_control(self):
        # Ici vous mettez votre logique de mouvement, avec les touches de clavier etc.
        if key.get_pressed()[K_UP]:
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= 1 * self.speed
        
        if key.get_pressed()[K_DOWN]:
            if self.rect.y >= self.screen.get_height() - 100:
                self.rect.y = self.screen.get_height() - 100
            else:
                self.rect.y += 1 * self.speed
        return

    # Imbattable, la raquette suis la balle directement sans faute
    def automatic_control(self):
        self.rect.y = self.ball.pos.y - 50
        
        if self.rect.y <= 0:
                self.rect.y = 0
        
        if self.rect.y >= self.screen.get_height() - 100:
                self.rect.y = self.screen.get_height() - 100
        return