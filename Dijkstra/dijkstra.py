import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def dijkstra(G, k=1):
    # A flag to deal with first node
    roots = random.sample(G.nodes, k)
    # List of nodes
    nodes = G.nodes()
    # Initializing all nodes with 'not visited', no parents and infinite value (except first node) for it's weight(cost)
    for node in nodes:
        if node in roots:
            nx.set_node_attributes(G, {node: 0},'min_path')
        else:
            nx.set_node_attributes(G, {node: float('inf')},'min_path')
        nx.set_node_attributes(G, {node: None},'parent')
        nx.set_node_attributes(G, {node: False},'visited')

    # Getting all nodes and it's attributes
    all_nodes = G.nodes(data=True)
    # While exists a non-visited node
    while any(node[1]['visited'] == False for node in all_nodes):
        # Create a list of nodes to be visited
        to_visit = []
        # Every non-visited node that has a parent can be visited now
        for node in all_nodes:
            if node[1]['visited'] == False:
                to_visit.append(node)

        parent_node = to_visit[0]
        # Finding lowest min_path
        for node in to_visit:
            if node[1]['min_path']< parent_node[1]['min_path']:
                parent_node = node

        # Get n's neighbors and it's attributes
        neighbors = G.neighbors(parent_node[0])

        # Checking if neighbor's path is the minimum
        for neighbor in neighbors:
            if G.node[neighbor]['visited'] ==  False:
                found_path = G.get_edge_data(parent_node[0], neighbor)['weight'] + parent_node[1]['min_path']
                # If neighbor's path is lower than actual value than change values and update parent node
                if found_path < G.node[neighbor]['min_path']:
                    G.node[neighbor]['min_path'] = found_path
                    G.node[neighbor]['parent'] = parent_node[0]

        # Setting parent to visited
        G.node[parent_node[0]]['visited'] = True

    # Creating MST after finding min path for all nodes
    mst = nx.Graph()
    for node in all_nodes:
        if node[1]['parent'] != None and node[1]['visited'] == True:
            # Get the parent of a node and a weight from parent to that node
            parent = node[1]['parent']
            weight = node[1]['min_path']

            mst.add_weighted_edges_from( [ [parent, node[0], weight] ] )
    return mst


def main():
    A = np.loadtxt('wg59_dist.txt')
    G = nx.from_numpy_matrix(A)

    mst = dijkstra(G,2)
    nx.draw_networkx(mst)
    plt.show()

    mst = dijkstra(G,3)
    nx.draw_networkx(mst)
    plt.show()

if __name__ == '__main__':
    main()
