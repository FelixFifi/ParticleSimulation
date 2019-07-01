from ParticlesSetup import random_gravity_particles
import tkinter as tk


class Window:

    def __init__(self, width, height, update_function, particles_generators):
        """

        :param width:
        :param height:
        :param update_function:
        :param particles_generators:
        """
        self.width = width
        self.height = height
        self.particles_generators = particles_generators
        self.selected_generator = particles_generators[0]
        self.update_function = update_function

        # ==== UI creation ====
        self.master = tk.Tk()
        self.master.title = "Particle Simulation"

        # Time scale
        self.update_time_ms_tk = tk.IntVar()
        self.update_time_ms_tk.set(10)
        self.scale_update = tk.Scale(self.master, variable=self.update_time_ms_tk, from_=0, to=1000,
                                     orient=tk.HORIZONTAL, length=width,
                                     label="(Minimum) Time between update calls [ms]")
        self.scale_update.grid()

        # Number of particles scale
        self.num_particles_tk = tk.IntVar()
        self.num_particles_tk.set(50)
        self.scale_num_particles = tk.Scale(self.master, variable=self.num_particles_tk, from_=0, to=500,
                                            orient=tk.HORIZONTAL, length=width, label="Number of particles")
        self.scale_num_particles.grid()

        # Main Canvas
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.grid()

        # Restart button
        self.button_restart = tk.Button(self.master, text="Restart", command=self.restart)
        self.button_restart.grid()

        # Events
        self.set_key_event_handlers()

        # ==== Initialization ====
        # Create particles
        self.particles = None
        self.restart()

        # Start regular update loop
        self.master.after(self.update_time_ms_tk.get(), func=self.update_wrapper)

        self.master.mainloop()

    def set_key_event_handlers(self):
        # Bind all number keys to particle type switching
        for i in range(1, 10):
            self.master.bind_all(str(i), self.switch_particle_types_handler)

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
        self.particles = self.selected_generator(self.num_particles_tk.get(), self.width, self.height)

    def update_wrapper(self):
        """
        Wraps the call to update function to end with another after statement to trigger it again
        :return:
        """
        self.particles = self.update_function(self.particles)
        self.draw()
        self.master.after(self.update_time_ms_tk.get(), func=self.update_wrapper)

    def switch_particle_types_handler(self, event):
        key = int(event.keysym)

        if key <= len(self.particles_generators):
            # First key is 1 but array starts at 0
            self.selected_generator = self.particles_generators[key - 1]
            self.restart()

