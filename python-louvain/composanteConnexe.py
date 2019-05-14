from igraph import *

g = Graph.Read_Ncol('3elt', directed=False)
largest = g.clusters().giant()
largest.save("lcc_3elt", format="edgelist")
