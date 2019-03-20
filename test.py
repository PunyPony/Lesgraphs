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
    shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
    nx.draw_shell(G, nlist=shells)
    plt.show()



G = read_graph("inet")
draw(G)
#gephi
#script_dir = os.path.dirname(__file__)
#print(script_dir)
#Fh = open(os.path.join(script_dir, '~/Downloads/lol.txt'), 'r')
#test_graph()
