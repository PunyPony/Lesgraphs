import networkx as nx
import matplotlib.pyplot as plt
import community
import time
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import numpy as np

def read_graph(path):
  mygraph = nx.read_edgelist(path)
  return mygraph

def draw(Gs):
    viridis = cm.get_cmap('viridis')
    color = iter(viridis(np.linspace(0, 1, len(Gs))))
    for G in Gs:
        nx.draw(G, with_labels=True, font_weight='bold',
                node_color=next(color))
    plt.show()

def best_partition(G):
    start = time.time()
    partition = community.best_partition(graph=G, randomize=False)
    end = time.time()
    print("partitioning took {}s".format(end - start))
    print(("nodes : {}, edges : {}, partition : {}").format(G.number_of_nodes(), G.number_of_edges(), len(partition)))



# https://networkx.github.io/documentation/latest/tutorial.html#multigraphs
# http://data.complexnetworks.fr/Diameter/
# https://python-louvain.readthedocs.io/en/latest/api.html#community.best_partition
# https://github.com/taynaud/python-louvain
# https://en.wikipedia.org/wiki/Louvain_Modularity
# grephi
# Calculer la composante connexe géante
# https://hal.archives-ouvertes.fr/hal-01171295/document

# G = nx.random_lobster(10, 0.9, 0.9)
# G = nx.barabasi_albert_graph(100, 5)
# G = nx.watts_strogatz_graph(5, 1, 0.1)
# G = nx.dodecahedral_graph()
# G = test_graph()


G = nx.erdos_renyi_graph(1000, 0.30)
G = max(nx.connected_component_subgraphs(G), key=len)
G = nx.OrderedGraph(G) # not necessary in python > 3.6

#G = read_graph("inet")
#print("G is a ",type(G), G.__dict__)
print("loaded")

best_partition(G)


bfs_order = list(nx.bfs_tree(G,0))
#print(bfs_order)

#print(G.node)

mapping = dict(zip(G.node, bfs_order))
#print(mapping)
H = nx.relabel.relabel_nodes(G, mapping)
best_partition(H)
#draw([G, H])

