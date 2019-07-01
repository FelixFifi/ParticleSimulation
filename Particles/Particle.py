from abc import ABC, abstractmethod
from random import randint
import numpy as np


class Particle(ABC):

    def __init__(self, position, color, canvas_width, canvas_height, radius=None):
        self.position = np.array(position, dtype=np.float)
        self.color = color

        if not radius:
            radius = 10
        self.radius = radius

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    @abstractmethod
    def update_position(self, particles):
        pass

    def draw(self, canvas):
        canvas.create_oval(self.position[0] - self.radius, self.position[1] - self.radius,
                           self.position[0] + self.radius, self.position[1] + self.radius,
                           fill=self.color, width=0)

    def distance(self, particle):
        return np.linalg.norm(self.position - particle.position)

    @staticmethod
    def random_color():
        """

        :return: (string) random color in the format #rrggbb
        """
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        return f"#{r:02x}{g:02x}{b:02x}"


def update_particles(particles):
    for i, particle in enumerate(particles):
        other_particles = particles[:i] + particles[i + 1:]
        particle.update_position(other_particles)

    return particles
