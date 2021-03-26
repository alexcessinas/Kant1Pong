from pygame import Surface, draw, Rect
from constants import colors, cell_size
from random import randrange

class Cell:

    color = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def init(self, screen: Surface):
        self.screen = screen
        return

    def update(self):
        draw.rect(self.screen, (randrange(256), randrange(256), randrange(256)), Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size))