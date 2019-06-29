from Window import Window
from random import randint, randrange
from Particles.InertialParticle import InertialParticle


def random_position(width, height):
    return [randint(0, width - 1), randint(0, height - 1)]


def random_velocity(max_v):
    return [randint(-max_v, max_v), randint(-max_v, max_v)]


def update_particles(particles):
    for i, particle in enumerate(particles):
        other_particles = particles[:i] + particles[i + 1:]
        particle.update(other_particles)

    return particles


def random_particles(num_particles, width, height):
    particles = []
    for i in range(num_particles):
        particle = InertialParticle(random_position(width, height), random_velocity(5), width, height)
        particles.append(particle)
    return particles


def main():
    width = 1024
    height = 768
    particles = random_particles(100, width, height)
    window = Window(width, height, update_particles, particles)


if __name__ == "__main__":
    main()
