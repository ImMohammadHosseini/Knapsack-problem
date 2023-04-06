"""

"""

from random import randint, random

class Ant:
    def __init__(self, status = 0):
        
        self.p = [status]
        
    def get_p (self):
        length = len(self.p)
        return [tuple(sorted((self.p[i], self.p[(i + 1) % length]), reverse=True))
            for i in range(length)]
        
    def get_wp(self, graph):
        
        w, p = graph.get_p_w(self.p)
        return w, p 
    
    def get_available(self, graph):
        nodes = set(range(len(graph.nodes)))
        available = nodes - set(self.p)
        twjs = self.twjs(graph)
        
        not_good = []    
        for _ in range(len(graph.nodes)):
            if twjs + graph.nodes[_].wj > graph.W:
                not_good.append(_)
        available -= set(not_good) 
        return available
        
    def cycle(self, graph):
        available = self.get_available(graph)
        
        counter = 0
        while available:
            counter += 1
            self.next_(graph, available)
            available = self.get_available(graph)
    
    def next_(self, graph, available):
        twjs = self.twjs(graph)
        '''for _ in self.p:
            twjs = graph.nodes[_].wj'''
        if len(available) == 1:
            a =  available.pop()
            #if twjs + graph.nodes[a].wj <= graph.W:
            self.p.append(a)

        if not available:
            return

        total = 0
        probabilities = {}
        for node_index in available:
            probabilities[node_index] = graph.get_probability(
                    self.p[-1], node_index)
            total += probabilities[node_index]
           

        threshold = random()
        probability = 0
        for node_index in available:
            probability += probabilities[node_index] / total
            if threshold < probability:
                self.p.append(node_index)
                return
        a =  available.pop()
        if twjs + graph.nodes[a].wj <= graph.W:
            self.p.append(a)
      
       
    def twjs (self, graph):
        twjs = 0
        for _ in self.p:
            twjs += graph.nodes[_].wj
        return twjs