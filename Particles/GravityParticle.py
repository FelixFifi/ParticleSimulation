from Particles.InertialParticle import InertialParticle

G = 6.67408 * pow(10, -11)


class GravityParticle(InertialParticle):

    def __init__(self, position, velocity, canvas_width, canvas_height, color=None, mass=None):

        InertialParticle.__init__(self, position, velocity, canvas_width, canvas_height, color, mass)

    def update_position(self, particles):
        for particle in particles:
            if issubclass(type(particle), GravityParticle):
                # Gravitational pull
                distance = self.distance(particle)

                if distance == 0:
                    continue

                acceleration = G * particle.mass / distance ** 2
                direction = particle.position - self.position

                self.velocity += acceleration * direction

        InertialParticle.update_position(self, particles)

