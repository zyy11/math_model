import igraph as ig
import matplotlib.pyplot as plt

g = ig.Graph(
    6,
    [(0,1),(0,2),(1,2),(1,3),(2,4),(3,5),(4,1),(4,3),(4,5)],
    directed=True
)
g.es["capacity"] = [3,5,1,4,2,5,1,3,2]

flow = g.maxflow(0, 5, capacity=g.es["capacity"])

print("Max flow:", flow.value)
print("Edge assignments:", flow.flow)

edge_label=[]
edge_width=[]
for i in range(len(flow.flow)):
    edge_label.append(str(int(flow.flow[i]))+"/"+str(g.es["capacity"][i]))
    edge_width.append(flow.flow[i]+0.5)


fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="auto",
    vertex_label=range(g.vcount()),
    vertex_color="lightblue",
    edge_label=edge_label,
    edge_width=edge_width,
)
plt.show()