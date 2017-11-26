import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    main()

def prim(G):
    first = True
    # List of visited nodes
    visited = []
    # List of nodes
    nodes = G.nodes()

    # Initializing all nodes with no parents and infinite value (except first node) for it's distance
    for node in nodes:
        if first:
            nx.set_node_attributes(G, {node: 0},'min_path')
            first = False
        else:
            nx.set_node_attributes(G, {node: float('inf')},'min_path')
        nx.set_node_attributes(G, {node: None},'parent')

    while


def main():
    A = np.loadtxt('ha30_dist.txt')
    G = nx.from_numpy_matrix(A)

    nx.draw_spring(G)
    plt.show()
