from Particles.Particle import Particle
import numpy as np


class InertialParticle(Particle):

    def __init__(self, position, velocity, canvas_width, canvas_height, color=None, mass=None):
        if not color:
            color = Particle.random_color()

        Particle.__init__(self, position, color, canvas_width, canvas_height)

        self.velocity = velocity

        if not mass:
            mass = self.radius * self.radius * np.pi
        self.mass = mass

        self.collision_handled = False
        self.collided_with = []

    def update_position(self, particles):
        # Remove all particles from list that are no longer overlapping
        for previously_colliding_particle in self.collided_with[:]:
            if not self.overlap(previously_colliding_particle):
                self.collided_with.remove(previously_colliding_particle)

        # Collide with all particles
        for particle in particles:
            self.collide(particle)

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        self.keep_in_canvas()

        self.collision_handled = False

    def collide(self, particle):
        """
        As collisions change the velocity of both particles, for each collision there is only one particle that handles
        the velocity update.
        :param particle:
        :return:
        """
        if self.collision_handled:
            return

        # Check if the particles collided previously without leaving each others circles
        # => Ignore
        if particle in self.collided_with:
            return

        # Check if particle even supports collision
        if issubclass(type(particle), InertialParticle):
            if self.overlap(particle):
                # Check if particle already collided with something
                if not particle.collision_handled:
                    velocity_old = self.velocity

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

                    self.collision_handled = True
                    particle.collision_handled = True

                    self.collided_with.append(particle)
                    particle.collided_with.append(self)

                    return

        return

    def overlap(self, particle):
        return self.distance(particle) < particle.radius + self.radius

    def keep_in_canvas(self):
        x = self.position[0]
        y = self.position[1]

        if x < 0:
            self.position[0] = - x
            self.velocity[0] *= -1
        if y < 0:
            self.position[1] = - y
            self.velocity[1] *= -1

        if x >= self.canvas_width:
            self.position[0] = 2 * self.canvas_width - x + 1
            self.velocity[0] *= -1
        if y >= self.canvas_height:
            self.position[1] = 2 * self.canvas_height - y + 1
            self.velocity[1] *= -1
