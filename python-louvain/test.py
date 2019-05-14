import networkx as nx
import matplotlib.pyplot as plt
import community as co
import time
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import numpy as np

def read_graph(path):
  mygraph = nx.read_edgelist(path, nodetype=int)
  return mygraph

def draw(Gs):
    viridis = cm.get_cmap('spring')
    color = iter(viridis(np.linspace(0, 1, len(Gs))))
    for G in Gs:
        nx.draw(G, with_labels=True, font_weight='bold',
                node_color=next(color))
    plt.show()

def draw_partition(partition, filename=None):
  cmap = cm.get_cmap('spring')
  size = float(len(set(partition.values())))
  pos = nx.spring_layout(G)
  count = 0.
  for com in set(partition.values()):
    count += 1.
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, node_color = [cmap(count/size)]) 
    nx.draw_networkx_edges(G, pos, alpha=0.5)
  
  if filename:
    plt.savefig(filename)
  #plt.show()

def best_partition(G):
    start = time.time()
    partition = co.best_partition(graph=G, randomize=False)
    end = time.time()
    print("partitioning took {}s".format(end - start))
    print(("Nodes : {}, Edges : {}, partition : {}").format(G.number_of_nodes(), G.number_of_edges(), len(set(partition.values()))))
    return partition


def study_dendrogram(G):
  dendrogram = co.generate_dendrogram(G)
  modularity_at_level = dict()
  print("Dendrogram has {} levels".format(len(dendrogram)))
  for level in range(len(dendrogram)):
    part = co.partition_at_level(dendrogram, level)
    print("Found {} communities at level {}".format(len(set(part.values())), level))
    modularity_at_level[level] = co.modularity(part, G)

  plt.plot(list(modularity_at_level.keys()), list(modularity_at_level.values()), linestyle='dotted', marker = 'o', markersize=8)
  plt.xlabel("l - Level")
  plt.ylabel("Q - Modularity")
  plt.show()
  return dendrogram

def reorder_with_bfs(G):
  bfs_order = list(nx.bfs_tree(G,list(G.nodes)[0]))
  mapping = dict(zip(G.node, bfs_order))
  H = nx.relabel.relabel_nodes(G, mapping)
  return H
  


# https://networkx.github.io/documentation/latest/tutorial.html#multigraphs
# http://data.complexnetworks.fr/Diameter/
# https://python-louvain.readthedocs.io/en/latest/api.html#community.best_partition
# https://github.com/taynaud/python-louvain
# https://en.wikipedia.org/wiki/Louvain_Modularity
# grephi
# Calculer la composante connexe géante
# https://hal.archives-ouvertes.fr/hal-01171295/document
# https://plot.ly/python/igraph-networkx-comparison/#networkx

# G = nx.random_lobster(10, 0.9, 0.9)
# G = nx.barabasi_albert_graph(100, 5)
# G = nx.watts_strogatz_graph(5, 1, 0.1)
# G = nx.dodecahedral_graph()
# G = nx.erdos_renyi_graph(5000, 0.15)
# G = nx.karate_club_graph()

G = read_graph("lcc_inet")
G = max(nx.connected_component_subgraphs(G), key=len)
G = nx.OrderedGraph(G) # not necessary in python > 3.6
print("Loaded !")

print(("Nodes : {}, Edges : {}").format(G.number_of_nodes(), G.number_of_edges()))

#partition = best_partition(G)
study_dendrogram(G)
#draw_partition(partition, "louvain_without_reordering.png")


# H = reorder_with_bfs(G)
# partition = best_partition(H)


  
    


#draw([G,H])
