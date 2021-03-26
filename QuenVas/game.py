from pygame import Surface, mouse
from constants import colors, cell_size, grid_size
from objects.player import Player
from objects.cell import Cell


class Game:
    
    player = Player()
    grid = []

    should_run = True

    def init(self, screen: Surface):
        self.player.init(screen)
        for x in range(grid_size):
            self.grid.append([])
            for y in range(grid_size):
                cell = Cell(x, y)
                self.grid[x].append(cell)
                cell.init(screen)


    def update(self):
        self.player.update()
        for x in range(grid_size):
            for y in range(grid_size):
                self.grid[x][y].update()