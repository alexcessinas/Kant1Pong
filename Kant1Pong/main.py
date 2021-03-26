import pygame
from pygame import event, display
from game import Game

pygame.init()
display.set_caption("Kant1Pong")

screen = display.set_mode((800, 600))
game = Game()

game.init(screen)

while game.should_run :
    for e in event.get():
        if e.type == pygame.QUIT:
            game.should_run = False
    
    screen.fill((0, 0, 0))
    game.update()
    display.update()
