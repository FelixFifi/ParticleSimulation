import numpy as np


def attract_and_repel(particle_self, particle_other):
    vectorial_difference = particle_other.position - particle_self.position

    distance = np.linalg.norm(vectorial_difference)
    if distance == 0:
        return np.zeros(2, dtype=np.float)

    direction = vectorial_difference / distance

    if distance < 30:
        return -direction * 2
    else:
        return direction


def repel(particle_self, particle_other):
    vectorial_difference = particle_other.position - particle_self.position

    distance = np.linalg.norm(vectorial_difference)
    if distance == 0:
        return np.zeros(2, dtype=np.float)

    direction = vectorial_difference / distance

    return direction / distance**2
