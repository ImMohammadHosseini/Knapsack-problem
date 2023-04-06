
class Graph():
    
    def __init__ (self, nodes, W, alpha=1, beta=3, d=.2, min_ph=.5, profit=.1,
                  b_profit=.5):
        self.nodes = nodes
        self.alpha = alpha
        self.beta = beta
        self.d = d
        self.min_ph = min_ph
        self.profit = profit
        self.b_profit = b_profit
        self.W = W
        
        self.weights = {}
        self.prof ={}
        self.phs = {}
        self.totalweights = 0
        
        for i, node in enumerate(self.nodes):
            for j in range(i):
                wis = node.sum_wi(self.nodes[j])
                self.totalweights += wis
        for i, node in enumerate(self.nodes):
            for j in range(len(self.nodes)):
                if i == j:
                    self.weights[(i,j)] = 0
                    self.prof[(i,j)] = 0
                    self.phs[(i,j)] = 0
                else:
                    self.weights[(i,j)] = self.nodes[j].wj
                    self.prof[(i,j)] = self.nodes[j].pj
                    self.phs[(i,j)] = min_ph
        
     
    def pheromones (self, answer):
        for i, j in answer:
            self.phs[(i,j)] *= self.d
            self.phs[(i,j)] += self.profit
            
    def get_pheromone(self, i, j):
        return self.phs.get((i,j))
    
    def update_phs(self, all_ants):
        
        for i in self.phs:
            self.phs[i] *= (1-self.d)
        '''
        for ant in all_ants.ants:
            weight, profit = self.get_p_w(ant.p)
            twjs = ant.twjs(self)
            if twjs <= self.W:
                
                if profit > all_ants.max_profit:
                    for pair in ant.get_p():
                        self.phs[pair] += self.b_profit / profit
        for pair in self.phs:
            self.phs[pair] = max(self.min_ph, self.phs[pair])'''
            
    def get_p_w(self, p):
        
        length = len(p)
        weight = 0
        profit = 0
        for i in range(length):
            weight += self.get_w(p[i], p[(i + 1) % length])
            
            profit += self.get_p(p[i], p[(i + 1) % length])
        return weight, profit
    
    def get_w(self, i, j):
        return self.weights.get((i, j))
    
    def get_p(self, i, j):
        return self.prof.get((i,j))
    
    def get_probability(self, i, j):
        
        return ((self.get_pheromone(i, j) ** self.alpha) *
            (self.get_p(i, j) ** self.beta))
    
    def find_best (self, n=100, m=200):
        
        take_object = []
        ants = All_ants(m, self.W)
        for i in range(n):
            ants.do_cycles(self)
            take_object = ants.best
            self.update_phs(ants)
        return take_object

