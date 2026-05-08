# main implementation of Material Point Method, written by hand, without using any libraries.

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from lib.solver import MPMSolver


MPM = MPMSolver()
MPM.grid_mass = 1.0
MPM.starting_velocity = 3.0
MPM.gravity = -9.8

domain_min = 0.0
domain_max = 5.0


fig, ax = plt.subplots()
ax.set_xlim(domain_min, domain_max)
ax.set_ylim(-1, 1)
ax.set_yticks([])
ax.set_title("1D MPM Particle Bounce")

particle_plot, = ax.plot([], [], "o", color="tab:blue")
ground_line, = ax.plot([domain_min, domain_max], [0, 0], color="black")


def _apply_boundary():
	if MPM.particle_position < domain_min:
		MPM.particle_position = domain_min
		MPM.grid_velocity = -MPM.grid_velocity
		MPM.starting_velocity = MPM.grid_velocity
	elif MPM.particle_position > domain_max:
		MPM.particle_position = domain_max
		MPM.grid_velocity = -MPM.grid_velocity
		MPM.starting_velocity = MPM.grid_velocity


def init():
	particle_plot.set_data([MPM.particle_position], [0])
	return particle_plot, ground_line


def update(_frame):
	MPM.step()
	_apply_boundary()
	particle_plot.set_data([MPM.particle_position], [0])
	return particle_plot, ground_line


animation = FuncAnimation(fig, update, init_func=init, interval=50, blit=True)
plt.show()