from graph import Graph

G = Graph()
v = G.insert_vertex(0, 0)
v1 = G.insert_vertex(1, 1)
v2 = G.insert_vertex(9, 3)
v3 = G.insert_vertex(2, 7)
v4 = G.insert_vertex(5, 3)

G.insert_edge(v, v1)
G.insert_edge(v, v2)
G.insert_edge(v, v4)
G.insert_edge(v2, v3)
G.insert_edge(v4, v3)
G.insert_edge(v2, v4)

#print(G.BFS(v))
#print(G.calculate_path(v))
#print(G.fpath(v, v3))
#print(G.find_path(v, v3, 7))