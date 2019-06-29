from abc import ABC, abstractmethod
from random import randint


class Particle(ABC):
    PARTICLE_RADIUS = 3

    def __init__(self, position, color, canvas_width, canvas_height):
        self.position = position
        self.color = color

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    @abstractmethod
    def update(self, particles):
        pass

    def draw(self, canvas):
        canvas.create_oval(self.position[0] - self.PARTICLE_RADIUS, self.position[1] - self.PARTICLE_RADIUS,
                           self.position[0] + self.PARTICLE_RADIUS, self.position[1] + self.PARTICLE_RADIUS,
                           fill=self.color, width=0)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        return f"#{r:02x}{g:02x}{b:02x}"
