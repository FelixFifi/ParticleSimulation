from Window import Window
from ParticlesSetup import *
from Particles.Particle import update_particles


def main():
    width = 1024
    height = 768
    particles_generators = [random_different_groups_parameterized_particles, random_identical_parameterized_particles,
                            random_repel_particles, random_attract_repel_particles, random_charged_particles,
                            random_gravity_particles]
    window = Window(width, height, update_particles, particles_generators)


if __name__ == "__main__":
    main()
