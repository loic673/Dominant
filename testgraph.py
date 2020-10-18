import networkx as nx
import os
import matplotlib.pyplot as plt
from networkx.algorithms.dominating import is_dominating_set
from networkx.algorithms.bipartite import is_bipartite
from networkx.algorithms.bipartite.matching import *
from networkx.algorithms.bipartite.covering import *


folder_path = "/Users/Loïc/Desktop/AlgoAvancé/Dominant/public_dataset/"
filename= "31_10_reg.graph"


# for filename in os.listdir(folder_path):

#     g = nx.read_adjlist(os.path.join(folder_path, filename))
#     # print("is {} bipartite : {}".format(filename, is_bipartite(g)))
#     test = g.number_of_nodes() == g.number_of_edges()
#     print("is {} circulent ? {}".format(filename, test))


g = nx.read_adjlist(os.path.join(folder_path, filename))


nx.draw_networkx(g)
plt.show()