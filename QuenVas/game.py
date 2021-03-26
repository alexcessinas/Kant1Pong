from pygame import Surface, mouse
from constants import colors
from player import Player

class Game:
    
    player = Player()

    should_run = True

    def init(self, screen: Surface):
        self.player.init(screen)
        return

    def update(self):
        self.player.update()
        return