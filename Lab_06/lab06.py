###############################################
# Daniel Monteiro Ribeiro                     #
# RA: 176231                                  #
# Laboratório 06 - Teoria dos Grafos          #
# Descrição: Coloração Gulosa de Vértices     #
###############################################

class Graph:
    def __init__(self):
        # Utiliza dicionário para armazenar a lista de adjacências
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def greedy_coloring(self):
        # Ordena os vértices inicialmente pelos rótulos (ordem crescente)
        # para garantir um desempate determinístico.
        vertices = sorted(list(self.adj.keys()))
        
        # Ordena os vértices de forma não crescente com base nos graus.
        # O sort do Python é estável e preserva a ordem dos rótulos em caso de empate.
        vertices.sort(key=lambda x: len(self.adj[x]), reverse=True)

        color = {}
        for v in vertices:
            # Identifica as cores já utilizadas pelos vizinhos do vértice atual
            used_colors = {}
            for neighbor in self.adj[v]:
                if neighbor in color:
                    used_colors[color[neighbor]] = True

            # Encontra a menor cor disponível (começando de 0)
            c = 0
            while c in used_colors:
                c += 1
            
            # Aloca o local (cor) para a solução (vértice)
            color[v] = c

        return color

def main():
    # Lê a primeira linha com o número m de pares
    m = int(input().strip())

    g = Graph()

    # Lê as m linhas seguintes
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    # Executa a coloração gulosa
    colors = g.greedy_coloring()

    # Saída impressa em ordem crescente dos rótulos
    for v in sorted(colors.keys()):
        print(f"{v} {colors[v]}")

if __name__ == "__main__":
    main()