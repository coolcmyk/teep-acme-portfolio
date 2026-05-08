import math

class MPMSolver:
    def __init__(self):

        self.gravity = 10
        self.time_step = 0.1
        self.cell_size = 1

        self.starting_velocity = 0
        self.particle_position = 1.2 # 1d case
        self.particle_mass = 1.0
        self.particle_velocity = self.starting_velocity
        self.particle_stress = 0.0

        self.grid_mass = 0.0
        self.grid_momentum = 0.0
        self.grid_velocity = 0.0
        self.grid_force = 0.0

    def _get_affected_nodes(self, particle_position):
        #say if the particle_position is 1.2 => will return 1, 2
        #if the particle_position is 1.5 => will return 1, 2 too
        #it will return the lower and upper bound of the grid nodes that are affected by the particle

        return math.floor(particle_position), math.ceil(particle_position)

    def _calculate_grid_mass(self, grid_mass):
        return grid_mass
    
    def _calculate_grid_momentum(self):
        return self.grid_mass * self.grid_velocity

    def _calculate_internal_force(self):
        return 0.0

    def _calculate_external_force(self):
        return self.grid_mass * self.gravity
    
        
    def _p2g(self):o
        # Map particle mass, momentum, and forces to grid (1D, single node accumulation).


        affected_nodes = self._get_affected_nodes(self.particle_position)

        self.grid_mass += self._calculate_grid_mass(self.particle_mass)
        self.grid_momentum += self.particle_mass * self.particle_velocity

        internal_force = self._calculate_internal_force()
        external_force = self._calculate_external_force()
        self.grid_force += internal_force + external_force
o
        return affected_nodes

    def _update_grid(self):
        # Update grid momentum and velocity using accumulated forces.


        self.grid_momentum += self.grid_force * self.time_step

        if self.grid_mass != 0:
            self.grid_velocity = self.grid_momentum / self.grid_mass

    def _g2p(self):
        # Map updated grid velocity back to particle and advect position.


        self.particle_velocity = self.grid_velocity
        self.particle_position += self.particle_velocity * self.time_step

    def _reset_grid(self):
        # Clear grid for the next step.


        self.grid_mass = 0.0
        self.grid_momentum = 0.0
        self.grid_velocity = 0.0
        self.grid_force = 0.0

    def step(self):
        # P2G -> Grid update -> G2P -> Reset


        self._reset_grid()
        self._p2g()
        self._update_grid()
        self._g2p()