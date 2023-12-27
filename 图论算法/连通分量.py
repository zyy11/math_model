import igraph as ig
import matplotlib.pyplot as plt
import random

random.seed(0)
g = ig.Graph.GRG(50, 0.15)

components = g.connected_components(mode='weak')

fig, ax = plt.subplots()
ig.plot(
    components,
    target=ax,
    palette=ig.RainbowPalette(),
    vertex_size=7,
    vertex_color=list(map(int, ig.rescale(components.membership, (0, 200), clamp=True))),
    edge_width=0.7
)
plt.show()