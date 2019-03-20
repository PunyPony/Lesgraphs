import networkx as nx
import matplotlib.pyplot as plt
import os
def read_graph(path):
  mygraph = nx.read_edgelist(path)
  return mygraph

def draw(G):
    nx.draw(G, with_labels=True, font_weight='bold')
    nx.draw_shell(G, with_labels=False, font_weight='bold')
    plt.show()

def test_graph():
    G = nx.dodecahedral_graph()
    return G
    #shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
    #nx.draw_shell(G, nlist=shells)
    #plt.show()



# grephi
# Calculer la composante connexe géante
#G = read_graph("inet")
#G = test_graph()

# G = nx.random_lobster(100, 0.9, 0.9)
# G = nx.barabasi_albert_graph(100, 5)
# G = nx.watts_strogatz_graph(30, 3, 0.1)
# G = nx.erdos_renyi_graph(100, 0.15)

print(G.number_of_nodes(), G.number_of_edges())
draw(G)

