###############################################################################
# Daniel Monteiro Ribeiro                                                     #
# RA: 176231                                                                  #
# Laboratório 05 - Teoria dos Grafos                                          #
# Descrição: Caminho Mínimo                                                   #
###############################################################################

import heapq as heap
from math import floor

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.weights = {}

    def add_vertex(self, v: int):
        if v not in self.adj_list:
            self.adj_list[v] = []
    
    def add_arc(self, u: int, v: int, w: int):
        self.add_vertex(u)
        self.add_vertex(v)
        
        if v not in self.adj_list[u]:
            pos_v = self.binary_search(self.adj_list[u], v)
            self.adj_list[u].insert(pos_v, v)
            self.weights[(u, v)] = w

    def get_size(self):
        m = 0
        for v in self.adj_list:
            m += len(self.adj_list[v])
        return m
    
    def get_order(self):
        return len(self.adj_list)

    def binary_search(self, lst: list, target: int) -> int:
        low, high = 0, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
    
    def reverse(self):
        g_rev = Graph()
        for u in self.adj_list:
            for v in self.adj_list[u]:
                w = self.weights[(u, v)]
                g_rev.add_arc(v, u, w)
        return g_rev

def dijkstra(g, start, final):
    # Initialize-Single-Source
    ## distances v.d
    d = {v: float('inf') for v in g.adj_list}
    ## predecessors v.p
    p = {v: None for v in g.adj_list}
    ## start.d = 0
    d[start] = 0

    Q = [(0, start)]

    while Q:
        dist_u, u = heap.heappop(Q)

        if dist_u > d[u]:
            continue

        for v in g.adj_list[u]:
            alt = d[u] + g.weights[(u, v)]

            if alt < d[v]:
                d[v] = alt
                p[v] = u
                heap.heappush(Q, (alt, v))

    return d, p

def reconstruct_path(p, final):
    path = []
    current = final # Distribution center vertex

    # reconstruct the path from final to start using predecessors
    while current is not None:
        path.append(current)
        current = p[current]

    return path
    
def calculate_path_weight(g, path):
    total_weight = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        total_weight += g.weights[(u, v)]
    return total_weight

def main():
    g = Graph()
    distribution_centers = []
    # all paths from distribution centers that have the product to the client
    paths = []

    # Number of arcs
    m: int = int(input())

    for _ in range(m):
        u, v, w = map(int, input().split())
        g.add_arc(u, v, w)

    # Number of distribution centers
    n: int = int(input())

    for _ in range(n):
        v, hasProduct = map(int, input().split())
        distribution_centers.append((v, hasProduct))

    # Client vertex
    client: int = int(input())

    # Reverse the graph to solve Single-destination shortest-path problem
    # The single-destination is the client vertex
    reversed_g = g.reverse()

    distances, predecessors = dijkstra(reversed_g, client, None)

    # If there is a product and a path from the distribution center to the client, add it to the paths list
    for v, hasProduct in distribution_centers:
        if hasProduct and distances[v] != float('inf'):
                path = reconstruct_path(predecessors, v)
                weight = calculate_path_weight(g, path)
                heap.heappush(paths, (weight, path))
                # print(f'Rota do centro de distribuicao {v} para o cliente {client}:')
                # print(' -> '.join(map(str, path)))
                # print(f'Peso total: {weight}')

    if not paths:
        print(f'Nao ha rotas para {client} ou o produto em estoque')
    else:
        best_weight, best_path = heap.heappop(paths)
        best_distribution_center = best_path[0]
        path_route_time = floor(best_weight / 100)
        print(f'{best_distribution_center} {path_route_time:}')
        print(' '.join(map(str, best_path)))

if __name__ == "__main__":
    main()