from Particles.Particle import Particle


class InertialParticle(Particle):

    def __init__(self, position, velocity, canvas_width, canvas_height, color=None):
        self.velocity = velocity

        if not color:
            color = Particle.random_color()

        Particle.__init__(self, position, color, canvas_width, canvas_height)

    def update(self, particles):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        self.keep_in_canvas()

    def keep_in_canvas(self):
        x = self.position[0]
        y = self.position[1]

        if x < 0:
            self.position[0] = - x
            self.velocity[0] *= -1
        if y < 0:
            self.position[1] = - y
            self.velocity[1] *= -1

        if x >= self.canvas_width:
            self.position[0] = 2 * self.canvas_width - x + 1
            self.velocity[0] *= -1
        if y >= self.canvas_height:
            self.position[1] = 2 * self.canvas_height - y + 1
            self.velocity[1] *= -1
