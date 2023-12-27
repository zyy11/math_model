import igraph as ig
import matplotlib.pyplot as plt

g = ig.Graph.Bipartite(
    [0, 0, 0, 0, 0, 1, 1, 1, 1],
    [(0, 5), (1, 6), (1, 7), (2, 5), (2, 8), (3, 6), (4, 5), (4, 6)]
)

matching = g.maximum_bipartite_matching()

matching_size = 0
print("Matching is:")
for i in range(5):
    print(f"{i} - {matching.match_of(i)}")
    if matching.is_matched(i):
        matching_size += 1
print("Size of maximum matching is:", matching_size)

fig, ax = plt.subplots(figsize=(7, 3))
ig.plot(
    g,
    target=ax,
    layout=g.layout_bipartite(),
    vertex_size=30,
    vertex_label=range(g.vcount()),
    vertex_color="lightblue",
    edge_width=[3 if e.target == matching.match_of(e.source) else 1.0 for e in g.es],
    edge_color=["red" if e.target == matching.match_of(e.source) else "black" for e in g.es]
)
plt.show()