from Particles.Particle import Particle
import numpy as np


class InertialParticle(Particle):

    def __init__(self, position, velocity, canvas_width, canvas_height, color=None, mass=None, elasticity=1.0):
        if not color:
            color = Particle.random_color()

        Particle.__init__(self, position, color, canvas_width, canvas_height)

        self.velocity = np.array(velocity, dtype=np.float)

        if not mass:
            mass = self.radius * self.radius * np.pi
        self.mass = mass

        self.elasticity = elasticity

    def update_position(self, particles):
        # Collide with all particles
        for particle in particles:
            self.collide(particle)

        self.position += self.velocity

        self.keep_in_canvas()

    def add_force(self, force):
        self.velocity += force / self.mass

    def collide(self, particle):
        """
        As collisions change the velocity of both particles, for each collision there is only one particle that handles
        the velocity update.
        :param particle:
        :return:
        """

        # Check if particle even supports collision
        if issubclass(type(particle), InertialParticle):
            if self.overlap(particle):
                self.separate(particle)

                m1 = self.mass
                m2 = particle.mass

                x1 = self.position
                x2 = particle.position

                v1 = self.velocity
                v2 = particle.velocity

                norm_dx = np.linalg.norm(x1 - x2)
                if norm_dx != 0:
                    self.velocity = v1 - 2 * m2 / (m1 + m2) * \
                                    np.dot(v1 - v2, x1 - x2) / norm_dx ** 2 * (x1 - x2)
                    particle.velocity = v2 - 2 * m1 / (m2 + m1) * \
                                        np.dot(v2 - v1, x2 - x1) / norm_dx ** 2 * (x2 - x1)

                    self.velocity *= self.elasticity
                    particle.velocity *= particle.elasticity

                return
        return

    def separate(self, particle):
        vectorial_distance = particle.position - self.position
        overlap = np.linalg.norm(vectorial_distance) - self.radius - particle.radius

        normalized_distance = vectorial_distance / np.linalg.norm(vectorial_distance)

        self.position += normalized_distance * 0.501 * overlap
        particle.position -= normalized_distance * 0.501 * overlap

    def overlap(self, particle):
        return self.distance(particle) < particle.radius + self.radius

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
