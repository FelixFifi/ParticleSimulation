from Window import Window
from ParticlesSetup import random_gravity_particles, random_charged_particles
from Particles.Particle import update_particles


def main():
    width = 1024
    height = 768
    particles_generators = [random_charged_particles, random_gravity_particles]
    window = Window(width, height, update_particles, particles_generators)


if __name__ == "__main__":
    main()
