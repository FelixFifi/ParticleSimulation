from Particles.CollidingParticle import CollidingParticle
import numpy as np


class ForceFunctionParticle(CollidingParticle):
    """
    A ForceFunctionParticle has a function that dictates what force it produces on other particles.
    """
    def __init__(self, position, force_function, canvas_width, canvas_height,
                 velocity=np.array([0, 0], dtype=np.float), color=None, mass=None, elasticity=1.0, radius=None,
                 friction=0.0):
        """

        :param self:
        :param position:
        :param force_function: (function(particle_self, particle_other) => force on other (np.array))
        :param canvas_width:
        :param canvas_height:
        :param velocity:
        :param color:
        :param mass:
        :param elasticity:
        :return:
        """
        CollidingParticle.__init__(self, position, velocity, canvas_width, canvas_height, color, mass, elasticity,
                                   radius=radius, friction=friction)

        self.force_function = force_function

    def update_position(self, particles):
        force = np.array([0.0, 0.0], dtype=np.float)

        for particle in particles:
            force += particle.get_force_on(self)

        self.velocity += force / self.mass

        CollidingParticle.update_position(self, particles)

    def get_force_on(self, particle):
        return self.force_function(self, particle)
