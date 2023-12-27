import igraph as ig
import matplotlib.pyplot as plt

mat=[[0,50,10,0,45,0],
     [0,0,15,0,10,0],
     [20,0,0,15,0,0],
     [0,20,0,0,35,0],
     [0,0,0,30,0,0],
     [0,0,0,3,0,0]
     ]
g=ig.Graph.Weighted_Adjacency(mat, mode='directed')

results = g.get_shortest_paths(0, to=3, weights=g.es["weight"], output="epath")

if len(results[0]) > 0:
    distance = 0
    for e in results[0]:
        distance += g.es[e]["weight"]
    print("Shortest weighted distance is: ", distance)
else:
    print("End node could not be reached!")

g.es['width'] = 0.5
g.es[results[0]]['width'] = 2.5

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout='circle',
    vertex_color='steelblue',
    vertex_label=range(g.vcount()),
    edge_width=g.es['width'],
    edge_label=g.es["weight"],
    edge_color='#666',
    edge_align_label=True,
    edge_background='white'
)
plt.show()