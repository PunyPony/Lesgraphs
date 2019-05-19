import networkx as nx
import matplotlib.pyplot as plt
import community as co
import time
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import numpy as np
from collections import OrderedDict


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
    plt.savefig("drawings/"+filename)
  plt.show()

def best_partition(G):
    start = time.time()
    partition = co.best_partition(graph=G, random_state=0)
    end = time.time()
    print("partitioning took {}s".format(end - start))
    print(("Nodes : {}, Edges : {}, partition : {}").format(G.number_of_nodes(), G.number_of_edges(), len(set(partition.values()))))
    return partition


def study_dendrogram(G, filename):
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
  if filename:
    plt.savefig("drawings/"+filename)
  plt.show()
  return dendrogram

def reorder_with_bfs(G):
  bfs_order = list(nx.bfs_tree(G,list(G.nodes)[0]))
  G._adj = dict((k, G._adj.get(k)) for k in bfs_order)
  return G

def bp_bsf_bp():
  graphname = "3elt"
  G = read_graph("graphFiles/"+graphname)
  G = max(nx.connected_component_subgraphs(G), key=len)
  #G = nx.OrderedGraph(G) # not necessary in python > 3.6
  print("Loaded !")
  print(("Nodes : {}, Edges : {}").format(G.number_of_nodes(), G.number_of_edges()))
  partition = best_partition(G)
  H = reorder_with_bfs(G)
  partition = best_partition(H)

if __name__ == '__main__':
  bp_bsf_bp()