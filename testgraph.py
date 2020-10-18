import networkx as nx
import os
import matplotlib.pyplot as plt
from networkx.algorithms.dominating import is_dominating_set

folder_path = "/Users/Loïc/Desktop/AlgoAvancé/public_dataset/"

filename = "03_10_bin.graph"


g = nx.read_adjlist(os.path.join(folder_path, filename))


all_nodes = set(g)

v = all_nodes.pop()

neighbors_nb = {}
for node in all_nodes :
    neighbors_nb[len(set(g[node]))] = node

max_node = neighbors_nb[max(neighbors_nb.keys())]
dominating_set = {max_node}
dominating_set.add(max_node)
all_nodes = all_nodes - set(g[max_node]) - {max_node}

while all_nodes :

    neighbors_nb = {}
    for node in all_nodes :
        neighbors_nb[len(set(g[node]))] = node

    max_node = neighbors_nb[max(neighbors_nb.keys())]
    dominating_set.add(max_node)
    all_nodes = all_nodes - set(g[max_node]) - {max_node}

print(dominating_set)


# dominated_nodes = set()
# remaining_nodes = all_nodes

# neighbors = {v : }

# while remaining_nodes:
#     # Choose an arbitrary node and determine its undominated neighbors.
#     v = remaining_nodes.pop()
#     undominated_neighbors = set(g[v]) - dominating_set
#     # Add the node to the dominating set and the neighbors to the
#     # dominated set. Finally, remove all of those nodes from the set
#     # of remaining nodes.
#     dominating_set.add(v)
#     dominated_nodes |= undominated_neighbors
#     remaining_nodes -= undominated_neighbors


# return dominating_set


nx.draw_networkx(g)

plt.show()