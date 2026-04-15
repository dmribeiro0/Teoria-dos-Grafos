class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v: str):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u: str, v: str):
        self.add_vertex(u)
        self.add_vertex(v)

        pos_u, exists_u = self.binary_search(self.adj_list[u], v)
        pos_v, exists_v = self.binary_search(self.adj_list[v], u)

        # só adiciona se não existir nos dois lados
        if not exists_u and not exists_v:
            self.adj_list[u].insert(pos_u, v)
            if u != v:
                self.adj_list[v].insert(pos_v, u)

    def get_size(self):
        m = 0
        for v in self.adj_list:
            m += len(self.adj_list[v])
        return m // 2

    def get_order(self):
        return len(self.adj_list)

    def get_min_deg(self):
        if not self.adj_list:
            return 0
        return min(len(self.adj_list[v]) for v in self.adj_list)

    def get_max_deg(self):
        if not self.adj_list:
            return 0
        return max(len(self.adj_list[v]) for v in self.adj_list)

    def get_avg_deg(self):
        if self.get_order() == 0:
            return 0.0
        return (self.get_size() * 2) / self.get_order()

    def get_deg_list(self):
        deg_list = []
        ordered_vertices = sorted(self.adj_list.keys())  # ORDEM LEXICOGRÁFICA
        for v in ordered_vertices:
            deg_list.append(len(self.adj_list[v]))
        return deg_list

    def print_graph(self):
        ordered_vertices = sorted(self.adj_list.keys())  # ORDEM LEXICOGRÁFICA
        for v in ordered_vertices:
            vizinhos = self.adj_list[v]
            formatacao = ", ".join(f"'{n}'" for n in vizinhos)
            print(f"{v}: [{formatacao}]")

    def search_edge(self, u: str, v: str):
        if u not in self.adj_list:
            return False
        _, exists_v = self.binary_search(self.adj_list[u], v)
        return exists_v

    def binary_search(self, neighbours: list, v: str):
        left = 0
        right = len(neighbours) - 1

        while left <= right:
            mid = (left + right) // 2

            if neighbours[mid] == v:
                return mid, True
            if neighbours[mid] < v:
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

# SAÍDA (tratamento igual ao do código aceito)
if graph.get_order() > 0:
    print(f"Order: {graph.get_order()}")
    print(f"Size: {graph.get_size()}")
    print(f"Min degree: {graph.get_min_deg()}")
    print(f"Max degree: {graph.get_max_deg()}")
    print(f"Average degree: {graph.get_avg_deg():.1f}")
    print(f"Degree list: {graph.get_deg_list()}")
else:
    print("Min degree: 0")
    print("Max degree: 0")
    print("Average degree: 0.0")
    print("Degree list: []")

# listas de adjacência
graph.print_graph()

# busca de aresta
print(has_edge_uv)
