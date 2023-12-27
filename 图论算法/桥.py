import igraph as ig
import matplotlib.pyplot as plt

g = ig.Graph(14, [(0, 1), (1, 2), (2, 3), (0, 3), (0, 2), (1, 3), (3, 4),
        (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (7, 9), (9, 10), (10 ,11),
        (11 ,7), (7, 10), (8, 9), (8, 10), (5, 12), (12, 13)])

bridges = g.bridges()

g.es["color"] = "gray"
g.es[bridges]["color"] = "red"
g.es["width"] = 0.8
g.es[bridges]["width"] = 1.2

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    vertex_size=30,
    vertex_color="lightblue",
    vertex_label=range(g.vcount())
)
plt.show()
