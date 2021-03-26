from pygame import Surface, mouse, key
from constants import colors, cell_size, grid_size
from objects.player import Player
from objects.cell import Cell
from pygame.constants import K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9
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

    def update(self):
        self.player.update()

        if mouse.get_pressed()[0]:
            if not self.player.l_mouse_pressed:
                self.player.l_mouse_pressed = True
                self.on_key_press()
                self.on_l_mouse_click()
        else:
            self.player.l_mouse_pressed = False

        for x in range(grid_size):
            for y in range(grid_size):

                self.grid[x][y].update()

    def on_l_mouse_click(self):
        x = floor(mouse.get_pos()[0] / cell_size)
        y = floor(mouse.get_pos()[1] / cell_size)
        cell: Cell = self.grid[x][y]
        cell.color = self.player.current_color
        return
    
    def on_key_press(self):
        if key.get_pressed()[K_0]:
            self.player.current_color = 0
        elif key.get_pressed()[K_1]:
            self.player.current_color = 1
        elif key.get_pressed()[K_2]:
            self.player.current_color = 2
        elif key.get_pressed()[K_3]:
            self.player.current_color = 3
        elif key.get_pressed()[K_4]:
            self.player.current_color = 4
        elif key.get_pressed()[K_5]:
            self.player.current_color = 5
        elif key.get_pressed()[K_6]:
            self.player.current_color = 6
        elif key.get_pressed()[K_7]:
            self.player.current_color = 7
        elif key.get_pressed()[K_8]:
            self.player.current_color = 8
        elif key.get_pressed()[K_9]:
            self.player.current_color = 9