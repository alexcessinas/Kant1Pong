import pygame
from pygame import event, display
from game import Game
from constants import grid_size, cell_size, colors

pygame.init()
display.set_caption("QuenVas")

screen = display.set_mode((grid_size * cell_size, grid_size * cell_size))
game = Game()

game.init(screen)

while game.should_run :
    for e in event.get():
        if e.type == pygame.QUIT:
            game.should_run = False
    
    screen.fill(colors[2])
    game.update()
    display.update()