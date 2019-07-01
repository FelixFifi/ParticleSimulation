from Particles.InertialParticle import InertialParticle
import numpy as np


class CollidingParticle(InertialParticle):

    def update_position(self, particles):
        # Collide with all particles
        for particle in particles:
            self.collide(particle)

        InertialParticle.update_position(self, particles)

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
        distance = np.linalg.norm(vectorial_distance)
        overlap = distance - self.radius - particle.radius

        if distance == 0:
            # In case of distance of zero, just push in x direction
            normalized_distance = np.array([1.0, 0], dtype=float)
        else:
            normalized_distance = vectorial_distance / distance

        self.position += normalized_distance * 0.501 * overlap
        particle.position -= normalized_distance * 0.501 * overlap

    def overlap(self, particle):
        return self.distance(particle) < particle.radius + self.radius
