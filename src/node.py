

class Node:
    
    def __init__(self, wj, pj):
        
        self.wj = wj
        self.pj = pj
    
    def sum_wi(self, node):
        return self.wj + node.wj
        
    def sum_pi(self, node):
        return self.pj + node.pj