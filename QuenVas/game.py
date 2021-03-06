from pygame import Surface, mouse, key
from constants import colors, cell_size, grid_size, server_base_url
from objects.player import Player
from objects.cell import Cell
from pygame.constants import K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9
from math import floor
from json import dumps
import requests

class Game:
    
    countFrames = 0
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
        if self.countFrames >= 1800:
            self.countFrames = 0
        
        self.on_key_press()
        if mouse.get_pressed()[0]:
            if not self.player.l_mouse_pressed:
                self.player.l_mouse_pressed = True
                self.on_l_mouse_click()
        else:
            self.player.l_mouse_pressed = False

        if self.countFrames <= 0:
            res = requests.get(f'{server_base_url}full').json()
            for x in range(grid_size):
                for y in range(grid_size):
                    self.grid[x][y].color = res[x][y]
            self.countFrames = 0

        for x in range(grid_size):
            for y in range(grid_size):
                self.grid[x][y].update()
                
        self.player.update()
        self.countFrames += 1

    def on_l_mouse_click(self):
        x = floor(mouse.get_pos()[0] / cell_size)
        y = floor(mouse.get_pos()[1] / cell_size)
        cell: Cell = self.grid[x][y]
        cell.color = self.player.current_color
        body = {
	        "x": cell.x,
	        "y": cell.y,
	        "color": cell.color
        }
        headers = { 'content-type': 'application/json' }
        requests.post(f'{server_base_url}place', dumps(body),headers=headers)
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