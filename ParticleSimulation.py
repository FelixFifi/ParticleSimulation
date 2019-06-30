from Window import Window
from ParticlesSetup import random_gravity_particles, random_charged_particles
from Particles.Particle import update_particles


def main():
    width = 1024
    height = 768
    window = Window(width, height, update_particles, random_charged_particles)


if __name__ == "__main__":
    main()
