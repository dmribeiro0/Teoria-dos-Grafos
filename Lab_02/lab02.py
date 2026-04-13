#########################################
# Daniel Monteiro Ribeiro               #
# RA: 176231                            #
# Laboratório 01 - Teoria dos Grafos    #
#########################################

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v: str):
        # Adiciona v se ele não existir no grafo
        if self.adj_list.get(v) is None:
            self.adj_list.update({v: []})

    def add_edge(self, u: str, v: str):
        # Adiciona u ou v se eles não existirem no grafo
        self.add_vertex(u)
        self.add_vertex(v)

        # Encontra a posição onde v deve ser inserido na lista de adjacências de u e vice-versa
        # Insere se a aresta não existir
        pos_u, exists_u = self.binary_search(self.adj_list[u], v)
        pos_v, exists_v = self.binary_search(self.adj_list[v], u)
        if not exists_u:
            self.adj_list[u].insert(pos_u, v)
        if not exists_v and u != v:
            self.adj_list[v].insert(pos_v, u)

    def get_size(self):
        # Retorna o número de arestas do grafo
        m = 0
        for v in self.adj_list:
            m += len(self.adj_list[v])
        return m // 2
    
    def get_order(self):
        # Retorna o número de vértices do grafo
        return len(self.adj_list)
    
    def get_min_deg(self):
        # Retorna o grau mínimo do grafo
        if not self.adj_list:
            return 0
        return min(len(self.adj_list[v]) for v in self.adj_list)
    
    def get_max_deg(self):
        if not self.adj_list:
            return 0
        return max(len(self.adj_list[v]) for v in self.adj_list)
    
    def get_avg_deg(self):
        # Retorna o grau médio do grafo (m)
        # Soma dos graus dos vértices (2m) dividido pelo número de vértices (n)
        if self.get_order() == 0:
            return 0.0
        return self.get_size() * 2 / self.get_order()
    
    def get_deg_list(self):
        # Retorna a lista de graus dos vértices do grafo
        deg_list = []
        ordered_vertices = sorted(self.adj_list.keys())
        for v in ordered_vertices:
            deg_list.append(len(self.adj_list[v]))
        return deg_list

    def print_graph(self):
        # Imprime o grafo no formato "v: [v1, v2, ...]" seguindo a ordem lexicográfica dos vértices
        ordered_vertices = sorted(self.adj_list.keys())
        for v in ordered_vertices:
            print(f"{v}: {self.adj_list[v]}")
    
    def search_edge(self, u: str, v: str):
        # Retorna True se a aresta (u, v) existir no grafo e False caso contrário
        if u not in self.adj_list:
            return False
        _, exists_v = self.binary_search(self.adj_list[u], v)
        return exists_v

    def binary_search(self, neighbours: list, v: str):
        # Busca binária para encontrar a posição onde v deve ser inserido na lista de adjacências de um vértice 
        # e se v já existe na lista
        length = len(neighbours)
        left = 0
        right = length-1
        
        while left <= right:
            mid = (left + right) // 2
            u = neighbours[mid]

            if u == v:
                return mid, True
            
            if u < v:
                left = mid + 1

            else:
                right = mid - 1
        return left, False
    
# Main

graph = Graph()

n = int(input())

for _ in range(n):
    u, v = input().split()
    graph.add_edge(u, v)

u, v = input().split()
has_edge_uv = graph.search_edge(u, v)

print(f"Order: {graph.get_order()}")
print(f"Size: {graph.get_size()}")
print(f"Min degree: {graph.get_min_deg()}")
print(f"Max degree: {graph.get_max_deg()}")
print(f"Average degree: {graph.get_avg_deg():.1f}")
print(f"Degree list: {graph.get_deg_list()}")
graph.print_graph()
print(has_edge_uv)