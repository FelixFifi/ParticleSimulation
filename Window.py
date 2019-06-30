from ParticlesSetup import random_gravity_particles
import tkinter as tk

NUM_PARTICLES = 50


class Window:

    def __init__(self, width, height, update_function, particles_generator):
        self.width = width
        self.height = height

        self.particles_generator = particles_generator
        self.particles = None
        self.restart()

        self.master = tk.Tk()
        self.master.title = "Particle Simulation"

        self.update_function = update_function
        self.update_time_ms = tk.IntVar()
        self.update_time_ms.set(10)
        self.scale_update = tk.Scale(self.master, variable=self.update_time_ms, from_=0, to=1000,
                                     orient=tk.HORIZONTAL, length=width)
        self.scale_update.grid()

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.grid()

        self.button_restart = tk.Button(self.master, text="Restart", command=self.restart)
        self.button_restart.grid()

        # Start regular update loop
        self.master.after(self.update_time_ms.get(), func=self.update_wrapper)

        self.master.mainloop()

    def draw(self):
        """

        :param particles: Tuple of position and color
        :return:
        """
        self.canvas.delete(tk.ALL)

        for particle in self.particles:
            particle.draw(self.canvas)

        self.master.update_idletasks()

    def restart(self):
        self.particles = self.particles_generator(NUM_PARTICLES, self.width, self.height)

    def update_wrapper(self):
        """
        Wraps the call to update function to end with another after statement to trigger it again
        :return:
        """
        self.particles = self.update_function(self.particles)
        self.draw()
        self.master.after(self.update_time_ms.get(), func=self.update_wrapper)
