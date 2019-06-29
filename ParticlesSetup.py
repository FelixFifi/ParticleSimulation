from random import randint, randrange
from Particles.InertialParticle import InertialParticle
import numpy as np


def random_position(width, height):
    return np.array([randint(0, width - 1), randint(0, height - 1)])


def random_velocity(max_v):
    return np.array([randint(-max_v, max_v), randint(-max_v, max_v)])


def random_particles(num_particles, width, height):
    particles = []
    for i in range(num_particles):
        particle = InertialParticle(random_position(width, height), random_velocity(5), width, height)
        particles.append(particle)
    return particles