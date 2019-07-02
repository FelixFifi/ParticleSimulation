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


def repel_1_div_r2(particle_self, particle_other):
    vectorial_difference = particle_other.position - particle_self.position

    distance = np.linalg.norm(vectorial_difference)
    if distance == 0:
        return np.zeros(2, dtype=np.float)

    direction = vectorial_difference / distance

    return direction / distance**2


def parameterized_force_function_type1(factor_repelling, distance_mode_change, max_strength_slopes, distance_force_end):
    """
    Inspired by the shown force function in
    "Particle Life - A Game of Life Made of Particles" (https://youtu.be/Z_zmZ23grXE?t=108)

    Shape:
    - 1/r repelling force until distance_mode_change,
    - then rising force from 0 to max_strength_slopes until half way point with distance_force_end
    - then decreasing force until distance_force_end

    :param factor_repelling:
    :param distance_mode_change:
    :param max_strength_slopes:
    :param distance_force_end:
    :return:
    """

    def force_function(particle_self, particle_other):
        vectorial_difference = particle_other.position - particle_self.position

        distance = np.linalg.norm(vectorial_difference)
        if distance == 0:
            return np.zeros(2, dtype=np.float)

        direction = vectorial_difference / distance

        if distance < particle_self.radius + particle_other.radius:
            distance = particle_self.radius + particle_other.radius

        strength = 0.0
        if distance < distance_mode_change:
            strength = factor_repelling / (distance + 1) - factor_repelling / (distance_mode_change + 1)
        elif distance < distance_mode_change + (distance_force_end - distance_mode_change) / 2.0:
            strength = (distance - distance_mode_change) * max_strength_slopes / ((distance_force_end - distance_mode_change) / 2.0)
        elif distance < distance_force_end:
            strength = (distance_force_end - distance) * max_strength_slopes / ((distance_force_end - distance_mode_change) / 2.0)

        return direction * strength

    return force_function
