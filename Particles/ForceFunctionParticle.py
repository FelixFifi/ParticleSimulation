from Particles.InertialParticle import InertialParticle
import numpy as np


class ForceFunctionParticle(InertialParticle):
    """
    A ForceFunctionParticle has a function that dictates what force it produces on other particles.
    """
    def __init__(self, position, force_function, canvas_width, canvas_height,
                 velocity=np.array([0, 0], dtype=np.float), color=None, mass=None, elasticity=1.0):
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
        InertialParticle.__init__(self, position, velocity, canvas_width, canvas_height, color, mass, elasticity)

        self.force_function = force_function

    def update_position(self, particles):
        force = np.array([0.0, 0.0], dtype=np.float)

        for particle in particles:
            force += particle.get_force_on(self)

        self.velocity += force / self.mass

        InertialParticle.update_position(self, particles)

    def get_force_on(self, particle):
        return self.force_function(self, particle)
