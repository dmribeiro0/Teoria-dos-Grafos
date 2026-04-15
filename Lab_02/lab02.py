#########################################
# Daniel Monteiro Ribeiro               #
# RA: 176231                            #
# Laboratório 02 - Teoria dos Grafos    #
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
    
    # Transforma lista de adjacências em matriz de adjacências
    def adj_matrix(self):
        n = self.get_order()
        adj_matrix = [[0] * n for _ in range(n)]

        ordered_vertices = sorted(self.adj_list.keys())
        for i in range(n):
            u = ordered_vertices[i]
            for j in range(n):
                v = ordered_vertices[j]
                adj_matrix[i][j] = 1 if v in self.adj_list[u] else 0
        return adj_matrix
    
# Retorna a quantidade de ciclos de comprimento exatamente quatro
def count_C4(adj_matrix, n):
    count = 0
    # Para cada combinação de quatro vértices, verifica se eles formam um ciclo de comprimento quatro
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    count += is_there_a_cycle(adj_matrix, i, j, k, l)
    return count

# Função alternativa com complexidade de tempo O(n^3), gerada por IA. Contudo, ainda não passa em todos os testes.
# def count_C4(adj_matrix, n):
#     count = 0

#     for u in range(n):
#         for v in range(u+1, n):
#             common = 0

#             # conta vizinhos em comum de u e v
#             for w in range(n):
#                 if adj_matrix[u][w] and adj_matrix[v][w]:
#                     common += 1

#             # adiciona número de C4 formados por esse par
#             if common >= 2:
#                 count += (common * (common - 1)) // 2

#     return count // 2


def is_there_a_cycle(adj_matrix, i, j, k, l):
    # Se o grau mínimo dos vértices for maior ou igual a 2, então eles formam ao menos um ciclo de comprimento quatro (demonstração no arquivo README.md)
    sum = 0
    sum += adj_matrix[i][i] + adj_matrix[i][j] + adj_matrix[i][k] + adj_matrix[i][l]
    sum += adj_matrix[j][i] + adj_matrix[j][j] + adj_matrix[j][k] + adj_matrix[j][l]
    sum += adj_matrix[k][i] + adj_matrix[k][j] + adj_matrix[k][k] + adj_matrix[k][l]
    sum += adj_matrix[l][i] + adj_matrix[l][j] + adj_matrix[l][k] + adj_matrix[l][l]
    if sum < 8:     # Se o grau mínimo dos vértices for menor que 2, então eles não formam um ciclo de comprimento quatro
        return 0
    elif sum <= 10: # Caso dos graus (2, 2, 2, 2) - o C4 -  ou (2, 2, 3, 3) formam um único ciclo de tamanho 4
        return 1
    elif sum <= 12: # Caso dos graus (3, 3, 3, 3) - o K4 - forma três ciclos de tamanho 4
        return 3
    return 0


# Main

graph = Graph()

n = int(input())

for _ in range(n):
    u, v = input().split()
    graph.add_edge(u, v)

print(f"{count_C4(graph.adj_matrix(), graph.get_order())}")