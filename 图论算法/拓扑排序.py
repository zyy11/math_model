import igraph as ig
import matplotlib.pyplot as plt

g = ig.Graph(
    edges=[(0, 1), (0, 2), (1, 3), (2, 4), (4, 3), (3, 5), (4, 5)],
    directed=True,
)

results = g.topological_sorting(mode='out')
print('Topological sort of g (out):', *results)

fig, ax = plt.subplots(figsize=(5, 5))
ig.plot(
    g,
    target=ax,
    layout='kk',
    vertex_size=25,
    edge_width=4,
    vertex_label=range(g.vcount()),
    vertex_color="white",
)
plt.show()