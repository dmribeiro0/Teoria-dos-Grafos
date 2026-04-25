###############################################################################
# Daniel Monteiro Ribeiro                                                     #
# RA: 176231                                                                  #
# Laboratório 03 - Teoria dos Grafos                                          #
# Descrição: Implementação do Código de Prufer (codificação e decodificação)  #
###############################################################################

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v: int):
        if v not in self.adj_list:
            self.adj_list[v] = []
    
    def add_edge(self, u: int, v: int):
        self.add_vertex(u)
        self.add_vertex(v)

        pos_v = self.binary_search(self.adj_list[u], v)
        pos_u = self.binary_search(self.adj_list[v], u)
        if v not in self.adj_list[u]:
            self.adj_list[u].insert(pos_v, v)
        if u not in self.adj_list[v] and u != v:
            self.adj_list[v].insert(pos_u, u)

    def remove_edge(self, u: int, v: int):
        # Remove a aresta entre u e v, se existir
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

        # Remove vértices isolados
        if len(self.adj_list[u]) == 0:
            del self.adj_list[u]
        if len(self.adj_list[v]) == 0:
            del self.adj_list[v]
    
    def get_size(self):
        m = 0
        for v in self.adj_list:
            m += len(self.adj_list[v])
        return m // 2
    
    def get_order(self):
        return len(self.adj_list)
    
    def get_deg_list(self):
        return [len(self.adj_list[v]) for v in self.adj_list]

    def binary_search(self, lst: list, target: int) -> int:
        low, high = 0, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
    
    def copy(self):
        new_graph = Graph()
        for v in self.adj_list:
            for neighbor in self.adj_list[v]:
                new_graph.add_edge(v, neighbor)
        return new_graph
    
    def print_graph(self):
        for v in sorted(self.adj_list.keys()):
            print(f"{v}: {self.adj_list[v]}")
    

# Codigo de Prufer
import heapq

def prufer_encode(tree: Graph) -> list:
    # cópia para não destruir o original
    t = tree.copy()

    n = len(t.adj_list)
    prufer_code = []

    # grau de cada vértice
    deg = {v: len(t.adj_list[v]) for v in t.adj_list}

    # heap com folhas
    leaves = [v for v in t.adj_list if deg[v] == 1]
    heapq.heapify(leaves)

    for _ in range(n - 2):
        leaf = heapq.heappop(leaves)

        # único vizinho da folha
        neighbor = t.adj_list[leaf][0]

        prufer_code.append(neighbor)

        # remove aresta
        t.remove_edge(leaf, neighbor)

        # atualiza graus
        deg[leaf] -= 1
        deg[neighbor] -= 1

        if deg[neighbor] == 1:
            heapq.heappush(leaves, neighbor)

    return prufer_code


# Decodificação do Código de Prufer
import heapq

def prufer_decode(code: list) -> Graph:
    tree = Graph()
    n = len(code) + 2

    deg = [1] * n
    for u in code:
        deg[u] += 1

    leaves = [i for i in range(n) if deg[i] == 1]
    heapq.heapify(leaves)

    for u in code:
        v = heapq.heappop(leaves)
        tree.add_edge(u, v)

        deg[u] -= 1
        if deg[u] == 1:
            heapq.heappush(leaves, u)

    u = heapq.heappop(leaves)
    v = heapq.heappop(leaves)
    tree.add_edge(u, v)

    return tree


__main__ = "__main__"
if __name__ == __main__:
    tree = Graph()
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        tree.add_edge(u, v)
    input_prufer_code = list(map(int, input().split()))

    prufer_code = prufer_encode(tree)
    print(" ".join(map(str, prufer_code)))
    
    tree_decoded = prufer_decode(input_prufer_code)
    tree_decoded.print_graph()
