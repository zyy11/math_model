import igraph as ig
import matplotlib.pyplot as plt

mat=[[0,3,0,0,0,2],
     [3,0,5,0,2,0],
     [0,5,0,1,0,0],
     [0,0,1,0,4,0],
     [0,2,0,4,0,1],
     [2,0,0,0,1,0]
     ]
g=ig.Graph.Weighted_Adjacency(mat, mode='undirected')

mst_edges = g.spanning_tree(weights=g.es["weight"], return_tree=False)

print("Minimum edge weight sum:", sum(g.es[mst_edges]["weight"]))

g.es["color"] = "lightgray"
g.es[mst_edges]["color"] = "midnightblue"
g.es["width"] = 1.0
g.es[mst_edges]["width"] = 3.0


fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    #layout="grid",
    vertex_color="lightblue",
    edge_width=g.es["width"],
    edge_label=g.es["weight"],
    edge_background="white",
    vertex_label=range(g.vcount())
)
plt.show()