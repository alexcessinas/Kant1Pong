from pygame import Surface, mouse
from constants import colors, cell_size, grid_size
from objects.player import Player
from objects.cell import Cell
from math import floor


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
        
        print(colors)


    def update(self):
        self.player.update()

        if mouse.get_pressed()[0]:
            if not self.player.l_mouse_pressed:
                self.player.l_mouse_pressed = True

                x = floor(mouse.get_pos()[0] / cell_size)
                y = floor(mouse.get_pos()[1] / cell_size)
                
                cell: Cell = self.grid[x][y]
                cell.color = self.player.current_color
        else:
            self.player.l_mouse_pressed = False

        for x in range(grid_size):
            for y in range(grid_size):

                self.grid[x][y].update()

    def on_l_mouse_click(self, cell: Cell):
        return