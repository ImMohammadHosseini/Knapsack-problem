
from src.node import Node
from src.graph import Graph

if __name__ == "__main__":
    nodes = []
    node0 = Node(10, 1000)
    nodes.append(node0)
    node1 = Node(20, 400)
    nodes.append(node1)
    node2 = Node(10, 50)
    nodes.append(node2)
    node3= Node(30, 100)
    nodes.append(node3)
    node4 = Node(20, 100)
    nodes.append(node4)
    g = Graph(nodes, W = 50)
    print( g.find_best(n = 20, m = 10))              
                