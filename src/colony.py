
"""

"""
from .ant import Ant
from random import randint, random


class All_ants:
    
    def __init__(self, m, W):
        self.ants = []
        self.A_counts = m
        self.W = W
        
        self.best = None
        self.min_sum = float("inf")
        self.max_profit = 0
        
        
    def reset_ants(self, graph):
        self.ants = []
        nodes = len(graph.nodes) - 1
        for _ in range(self.A_counts):
            self.ants.append(Ant(randint(0, nodes)))

    def do_cycles(self, graph):
        twjs = 0
        
        self.reset_ants(graph=graph)
        for ant in self.ants:
            
            ant.cycle(graph=graph)
            twjs = ant.twjs(graph)
            graph.pheromones(answer = ant.get_p())
            weight, profit = ant.get_wp(graph=graph)
            if self.max_profit < profit:
                if twjs <= graph.W:
                    self.max_profit = profit
                    self.best = ant.p[:]