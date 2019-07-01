from Particles.CollidingParticle import CollidingParticle
import numpy as np

COULOMBS_CONSTANT = 8.99 * 10 ** 9


class ChargedParticle(CollidingParticle):

    def __init__(self, position, velocity, charge, canvas_width, canvas_height, mass=None, elasticity=1.0):
        self.charge = charge

        if charge > 0:
            color = "#ff0000"
        elif charge < 0:
            color = "#0000ff"
        else:
            color = "#ffffff"

        CollidingParticle.__init__(self, position, velocity, canvas_width, canvas_height, color, mass, elasticity)

    def update_position(self, particles):
        CollidingParticle.update_position(self, particles)

        force = np.array([0.0, 0.0], dtype=np.float)
        for particle in particles:
            if not issubclass(type(particle), ChargedParticle):
                continue
            vectorial_distance = particle.position - self.position
            force -= COULOMBS_CONSTANT * self.charge * particle.charge / np.linalg.norm(vectorial_distance) ** 2 \
                    * vectorial_distance

        self.velocity += force / self.mass

