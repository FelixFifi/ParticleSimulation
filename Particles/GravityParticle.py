from Particles.CollidingParticle import CollidingParticle

G = 6.67408 * pow(10, -11)


class GravityParticle(CollidingParticle):

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

        CollidingParticle.update_position(self, particles)

