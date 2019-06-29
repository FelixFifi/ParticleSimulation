from Window import Window
from ParticlesSetup import random_particles
from Particles.Particle import update_particles


def main():
    width = 1024
    height = 768
    particles = random_particles(100, width, height)
    window = Window(width, height, update_particles, particles)


if __name__ == "__main__":
    main()
