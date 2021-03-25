from pygame import Vector2, Surface, draw

class Ball:

    def __init__(self, pos = Vector2(0, 0)):
        self.pos = pos
        self.dir = Vector2(0, 0.5)
        self.speed = 0.2
        self.size = 5

    def init(self, screen: Surface):
        self.screen = screen
        self.pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)

    def update(self):
        # Update pos ball
        max_height = self.screen.get_height() - self.size
        min_height = self.size

        if self.pos.y >= max_height or self.pos.y <= min_height:
            self.speed = -self.speed

        self.pos += self.dir * self.speed

        draw.circle(self.screen, (255, 255, 255), self.pos, self.size)