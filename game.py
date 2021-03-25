from objects.ball import Ball
from pygame import Surface

class Game:

    ball = Ball()

    should_run = True

    def init(self, screen: Surface):
        self.ball.init(screen)

    def update(self):
        self.ball.update()

        # Collision Ball/Pads