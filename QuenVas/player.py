from pygame import Surface, mouse, draw

class Player:

    l_mouse_pressed = False

    def __init__(self):
        return

    def init(self, screen: Surface):
        self.screen = screen

    def update(self):
        draw.circle(self.screen, (0, 255, 0), mouse.get_pos(), 5)
        if mouse.get_pressed()[0]:
            draw.circle(self.screen, (255, 0, 0), mouse.get_pos(), 5)
            if not self.l_mouse_pressed:
                self.l_mouse_pressed = True
                self.on_l_mouse_click()
        else:
            self.l_mouse_pressed = False

    def on_l_mouse_click(self):
        print('Left click')