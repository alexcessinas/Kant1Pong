from objects.paddle import Paddle
from pygame.surface import Surface
from objects.ball import Ball

class Game:

    ball = Ball()
    player_paddle = Paddle(ball, True)
    enemy_paddle = Paddle(ball, False, 794)
    
    should_run = True

    def init(self, screen: Surface):
        self.ball.init(screen)
        self.player_paddle.init(screen)
        self.enemy_paddle.init(screen)

    def update(self):
        self.ball.update()
        self.player_paddle.update()
        self.enemy_paddle.update()
        # Collision Ball/Pads