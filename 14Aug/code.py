class Dynamics:
    def __init__(self):
        self.dim = 2
        self.num_particles = 64
        self.positions = np.zeros((self.num_particles,self.dim))
        self.velocities = np.zeros((self.num_particles,self.dim))
        self.mass = 1
        self.T = 1
        self.box_len = 10
        self.k = 1
        self.eps = 1
        self.sigma = 1
        self.dt = 0.001
        self.steps = 2000
    def position_init(self):
        self.positions = np.random.random_sample((self.num_particles,self.dim)) * self.box_len
    def velocity_init(self):
        factor = math.sqrt(self.k * self.T / self.mass)
        self.velocities = np.random.normal(loc=0,scale=factor,size=(self.num_particles, self.dim))
    def lj_force_pair(self,p1, p2):
        # force on p1 due to p2
        r = self.positions[p1] - self.positions[p2]
        r_mag = np.linalg.norm(r)
        r_cap = r/r_mag

        f_mag = 24*self.eps/r_mag * (2*((self.sigma/r_mag)**12) - (self.sigma/r_mag)**6)
        return f_mag * r_cap
        
    def lj_force(self, p):
        force = np.zeros(shape=2)
        for part in range(self.num_particles):
            if(part == p):
                continue
            force += self.lj_force_pair(p, part)
        return force
    def euler_integrate(self):
        for i in range(self.steps):
            forces = np.array([self.lj_force(p) for p in range(self.num_particles)])
            self.positions = self.positions + self.velocities*self.dt
            self.velocities = self.velocities + forces*(self.dt/self.mass)
    
    def draw_particles(self):
        plt.figure(figsize=(5,5))
        axis = plt.gca()
        
        axis.set_xlim(-10,self.box_len+10)
        axis.set_ylim(-10,self.box_len+10)

        for i in range(self.num_particles):
            axis.add_patch( plt.Circle(self.positions[i], radius=0.5, 
                                                   linewidth=2, edgecolor='black') )
        plt.show()
    def pe_pair(self, p1, p2):
        r = self.positions[p1] - self.positions[p2]
        r_mag = np.linalg.norm(r)
        
        return 4*self.eps*((self.sigma/r_mag)**12 - (self.sigma/r_mag)**6)
    def pe(self):
        total_pe = 0.0
        for i in range(self.num_particles):
            for j in range(i+1, self.num_particles):
                total_pe += self.pe_pair(i,j)
        return total_pe
    
    def minimize(self, min_steps, max_dr = 0.15):
        for i in range(min_steps):
            p = np.random.randint(0,self.num_particles)
            dr = np.random.random_sample(size=2)*2*max_dr - max_dr
            pe_bef = self.pe()
            self.positions[p] += dr
            pe_after = self.pe()
            if(pe_bef < pe_after):
                self.positions[p] -= dr


