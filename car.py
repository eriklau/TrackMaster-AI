from pyglet.sprite import Sprite
from pyglet.window import key

class Car:
    def __init__(self, image, batch) -> None:
        image.anchor_x = 25
        image.anchor_y = 25
        self.body = Sprite(image, batch=batch)
        self.body.x, self.body.y = 480, 260
        self.speed = 0.0

    def update(self, delta_time, keyboard):
        acceleration = 0.0
        if keyboard[key.UP]:
            acceleration = 1.0

        if acceleration > 0:
            self.speed += 0.1

        self.body.x += self.speed