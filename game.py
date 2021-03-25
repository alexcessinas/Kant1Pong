import pygame
from pygame import display, draw, event, key
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN

screen = display.set_mode((800,600))
running = True


def init():
    pygame.init()


def update():
    for e in event.get():
        if e.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    # Le jeu

    display.update()