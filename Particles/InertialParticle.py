from Particles.Particle import Particle
import numpy as np


class InertialParticle(Particle):

    def __init__(self, position, velocity, canvas_width, canvas_height, color=None, mass=None, elasticity=1.0,
                 radius=None, friction=0.0):
        if not color:
            color = Particle.random_color()

        Particle.__init__(self, position, color, canvas_width, canvas_height, radius=radius)

        self.velocity = np.array(velocity, dtype=np.float)
        self.friction = friction

        if not mass:
            mass = self.radius * self.radius * np.pi
        self.mass = mass

        self.elasticity = elasticity

    def update_position(self, particles):
        self.position += self.velocity

        self.velocity *= 1 - self.friction

        self.keep_in_canvas()

    def add_force(self, force):
        self.velocity += force / self.mass

    def keep_in_canvas(self):
        x = self.position[0]
        y = self.position[1]

        if x < 0:
            self.position[0] = - x
            self.velocity[0] *= -self.elasticity
        if y < 0:
            self.position[1] = - y
            self.velocity[1] *= -self.elasticity

        if x >= self.canvas_width:
            self.position[0] = 2 * self.canvas_width - x + 1
            self.velocity[0] *= -self.elasticity
        if y >= self.canvas_height:
            self.position[1] = 2 * self.canvas_height - y + 1
            self.velocity[1] *= -self.elasticity
