# Dictionary
# graph = {}

# v = "v1"

# graph.update({"v0": []})
# graph.update({v: []})


# print(graph.keys())
# print(graph)

# neighbors = graph[v]

# print(neighbors)

# neighbors.append("v2")

# neighbors.append("v0")

# neighbors.append(v)

# print(neighbors)

# neighbors.sort()
# neighbors = sorted(neighbors)

# print(neighbors)
# print(graph[v])

# graph.update({v: neighbors})

# print(graph)

# m = 0
# for v in graph:
#     print(v)
#     print(graph[v])
#     m += len(graph[v])

# print(m)

# n = 0
# for v in graph:
#     n+=1

# print(n)

# print(next(iter(graph.values())))

# graph.update({"v4": []})
# graph.update({"v3": []})

# print(graph)
# print(sorted(graph))
# print(graph)
# print(graph)

# print(7//2)

# print("v0" > "v1")

# u = "v12"
# index = u[1:]
# print(index)
# print(int(index))


# adj_list = {
#     "v0": ["v1", "v2"],
#     "v1": ["v0", "v2"],
#     "v2": ["v0", "v1", "v3"],
#     "v3": ["v2"]
# }


# print(min(len(adj_list[v]) for v in adj_list))
# print(max(len(adj_list[v]) for v in adj_list))

# # (v0, v1, v2, v3, v0)

# adj_matrix = [#  v0 v1 v2 v3
#                 [0, 1, 0, 1],   # v0
#                 [1, 0, 1, 0],   # v1
#                 [0, 1, 0, 1],   # v2
#                 [1, 0, 1, 0]]   # v3


# # (v0, v2, v1, v3, v0)

# adj_matrix2 = [# v0 v1 v2 v3
#                 [0, 0, 1, 1],   # v0
#                 [0, 0, 1, 1],   # v1
#                 [1, 1, 0, 0],   # v2
#                 [1, 1, 0, 0]]   # v3

# adj_matrix3 = [# v1 v2 v3 v4 v5 v6 v7 v8 v9 v10
#                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],   # v1
#                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],   # v2
#                 [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],   # v3
#                 [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],   # v4
#                 [0, 0, 1, 1, 0, 0, 0, 0, 1, 0],   # v5
#                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],   # v6
#                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],   # v7
#                 [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],   # v8
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],   # v9
#                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]   # v10

# adj_matrix4 = [ #v2 v4 v6 v8
#                 [0, 1, 0, 0],   # v2
#                 [1, 0, 1, 0],   # v4
#                 [0, 1, 0, 1],   # v6
#                 [0, 0, 1, 0]]   # v8 

# To know if there is a cycle based on an adjacency matrix, we need to check if there is a path from a vertex to itself.
# Particularly, if we want to know if there is a length 4 cycle we need to check if there is a 4 length path (4 edges)
# An algorithm for that, could be, to every vertex on the graph, walk every four length path from that vertex 
# and check if it ends on the same vertex. If it does, there is a cycle of length 4 in the graph, from that vertex.

# First thing we can do is an algorithm to walk every path of length 4 from a vertex.

# adj_matrix = [[0] * 3 for _ in range(3)]

# print(adj_matrix)

def to_adj_matrix(adj_list, n):
    adj_matrix = [[0] * n for _ in range(n)]

    ordered_vertices = sorted(adj_list.keys())
    for i in range(n):
        u = ordered_vertices[i]
        for j in range(n):
            v = ordered_vertices[j]
            adj_matrix[i][j] = 1 if v in adj_list[u] else 0
    return adj_matrix

adj_list = {
    "v0": ["v1", "v2"],
    "v1": ["v0", "v2"],
    "v2": ["v0", "v1", "v3"],
    "v3": ["v2"]
}

adj_matrix = to_adj_matrix(adj_list, 4)

print(adj_matrix)