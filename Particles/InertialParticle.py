from Particles.Particle import Particle
import numpy as np


class InertialParticle(Particle):

    def __init__(self, position, velocity, canvas_width, canvas_height, color=None, mass=None, elasticity=1.0,
                 radius=None, friction=0.0):
        if not color:
            color = Particle.random_color()

        Particle.__init__(self, position, color, canvas_width, canvas_height, radius=radius)
        self.canvas_center = np.array([self.canvas_width / 2.0 - 0.5, self.canvas_height / 2.0 - 0.5], dtype=np.float)

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
            self.position[0] = 2 * self.canvas_width - x
            self.velocity[0] *= -self.elasticity
        if y >= self.canvas_height:
            self.position[1] = 2 * self.canvas_height - y
            self.velocity[1] *= -self.elasticity

        # Add force towards center if very close to border
        distance_to_border = self._distance_to_border()
        force_end = 50
        force_strength = 5

        if distance_to_border <= force_end:
            vector_center = self.canvas_center - self.position
            direction_center = vector_center / np.linalg.norm(vector_center)

            force = force_strength * (direction_center / (distance_to_border + 1))
            force += np.sign(force) * force_strength / force_end
            self.add_force(force)

    def _distance_to_border(self):
        x = self.position[0]
        y = self.position[1]
        return min(x, y, self.canvas_width - x, self.canvas_height - y)
