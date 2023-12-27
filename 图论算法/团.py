import igraph as ig
import matplotlib.pyplot as plt

g = ig.Graph.Famous('Zachary')

cliques = g.cliques(4, 4)

fig, axs = plt.subplots(3, 4)
axs = axs.ravel()
for clique, ax in zip(cliques, axs):
    ig.plot(
        ig.VertexCover(g, [clique]),
        mark_groups=True, palette=ig.RainbowPalette(),
        vertex_size=5,
        edge_width=0.5,
        target=ax,
    )
plt.axis('off')
plt.show()
