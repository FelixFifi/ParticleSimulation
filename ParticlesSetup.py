from random import randint, randrange
from Particles.GravityParticle import GravityParticle
import numpy as np


def random_position(width, height):
    return np.array([randint(0, width - 1), randint(0, height - 1)], dtype=np.float)


def random_velocity(max_v):
    return np.array([randint(-max_v, max_v), randint(-max_v, max_v)], dtype=np.float)


def random_particles(num_particles, width, height):
    particles = []
    for i in range(num_particles):
        particle = GravityParticle(random_position(width, height), np.array([0.0, 0.0], dtype=np.float), width, height, mass=4000000000)
        particles.append(particle)
    return particles