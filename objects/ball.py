from pygame import Vector2, Surface, draw, mixer, Rect
from pygame.mixer import Sound
from random import randint

class Ball:

    def __init__(self, pos = Vector2(0, 0)):
        mixer.init()
        self.pos = pos
        self.dir = Vector2(1, 1)
        self.speed = 0.2
        self.size = 6
        self.effect = Sound("assets/sounds/pong.wav")

    def init(self, screen: Surface):
        self.screen = screen
        self.pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)

    def update(self):
        max_height = self.screen.get_height() - self.size
        max_width = self.screen.get_width() - self.size
        min_height = min_width = self.size

        if self.pos.y >= max_height or self.pos.y <= min_height:
            self.dir.y = -self.dir.y
            self.effect.play()

        if self.pos.x >= max_width or self.pos.x <= min_width:
            self.pos = Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
            rand_dir_x = 1 if randint(0, 1) == 1 else -1
            rand_dir_y = 1 if randint(0, 1) == 1 else -1
            self.dir = Vector2(rand_dir_x, rand_dir_y)

        self.pos += self.dir * self.speed

        draw.circle(self.screen, (255, 255, 255), self.pos, self.size)
        draw.rect(self.screen, (0, 255, 0), self.get_collision_square())

    def get_collision_square(self):
        return Rect(self.pos.x - self.size, self.pos.y - self.size, self.size * 2, self.size * 2);