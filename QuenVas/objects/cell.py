from pygame import Surface, draw, Rect
from constants import colors, cell_size
from random import randrange

class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 0

    def init(self, screen: Surface):
        self.screen = screen
        return

    def update(self):
        draw.rect(self.screen, colors[self.color], self.get_block_colliders())

    def get_block_colliders(self):
        return Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)