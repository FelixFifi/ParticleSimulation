from random import randint, randrange, choice
from Particles.GravityParticle import GravityParticle
from Particles.ChargedParticle import ChargedParticle
from Particles.ForceFunctionParticle import ForceFunctionParticle
from ForceFunctions import *

import numpy as np


def random_position(width, height):
    return np.array([randint(0, width - 1), randint(0, height - 1)], dtype=np.float)


def random_velocity(max_v):
    return np.array([randint(-max_v, max_v), randint(-max_v, max_v)], dtype=np.float)


def random_gravity_particles(num_particles, width, height):
    particles = []
    for i in range(num_particles):
        elasticity = 0.5
        mass = 4000000000
        velocity = np.array([0.0, 0.0], dtype=np.float)
        position = random_position(width, height)
        particle = GravityParticle(position, velocity, width, height,
                                   mass=mass, elasticity=elasticity)
        particles.append(particle)
    return particles


def random_charged_particles(num_particles, width, height):
    particles = []

    charge_strength = 0.00001
    charges = [-charge_strength, charge_strength]
    for i in range(num_particles):
        position = random_position(width, height)
        velocity = np.array([0.0, 0.0], dtype=np.float)

        charge = choice(charges)
        particle = ChargedParticle(position, velocity, charge, width, height, mass=1, elasticity=0.5)
        particles.append(particle)
    return particles


def random_attract_repel_particles(num_particles, width, height):
    particles = []

    force_function = attract_and_repel
    for i in range(num_particles):
        position = random_position(width, height)
        velocity = np.array([0.0, 0.0], dtype=np.float)

        particle = ForceFunctionParticle(position, force_function, width, height, mass=1, elasticity=0.5)
        particles.append(particle)
    return particles

def random_repel_particles(num_particles, width, height):
    particles = []

    force_function = repel
    for i in range(num_particles):
        position = random_position(width, height)
        velocity = np.array([0.0, 0.0], dtype=np.float)

        particle = ForceFunctionParticle(position, force_function, width, height, mass=1, elasticity=0.5)
        particles.append(particle)
    return particles
