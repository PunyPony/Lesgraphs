import networkx as nx
import matplotlib.pyplot as plt
import community
import time

def read_graph(path):
  mygraph = nx.read_edgelist(path)
  return mygraph

def draw(G):
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def test_graph():
    G = nx.dodecahedral_graph()
    return G
    #shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
    #nx.draw_shell(G, nlist=shells)
    #plt.show()


# https://networkx.github.io/documentation/latest/tutorial.html#multigraphs
# http://data.complexnetworks.fr/Diameter/
# https://python-louvain.readthedocs.io/en/latest/api.html#community.best_partition
# https://github.com/taynaud/python-louvain
# https://en.wikipedia.org/wiki/Louvain_Modularity
# grephi
# Calculer la composante connexe géante

# G = nx.random_lobster(10, 0.9, 0.9)
# G = nx.barabasi_albert_graph(100, 5)
# G = nx.watts_strogatz_graph(5, 1, 0.1)
G = nx.erdos_renyi_graph(10, 0.15)
Go = nx.OrderedGraph(G) # not necessary in python > 3.6
# G = test_graph()



#G = read_graph("inet")
#print("G is a ",type(G), G.__dict__)
print("loaded")
partition1 = community.best_partition(graph=G, randomize=False)
start = time.time()
partition2 = community.best_partition(graph=G, randomize=False)
end = time.time()
print(end - start)
print(("nodes : {}, edges : {}, partition1 : {}, partition2 : {} equals : {}").format(G.number_of_nodes(), G.number_of_edges(), len(partition1), len(partition2), partition1==partition2))
#print(partition1, partition2)
#draw(G)

