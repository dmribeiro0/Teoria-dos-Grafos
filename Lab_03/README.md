# Teoria dos Grafos 2026 (1S) — Laboratório 3

---

## Descrição

Implemente uma solução para computar:

1. O Código de Prüfer de uma árvore.
2. Uma árvore a partir de um Código de Prüfer.

Os rótulos dos vértices devem se iniciar em zero. A implementação utiliza a classe `Graph` desenvolvida nos laboratórios anteriores, com a adição do método de remoção de arestas (`remove_edge`) e de métodos auxiliares necessários para manter a lista de adjacência ordenada e facilitar a manipulação do grafo.

## Como os algoritmos foram implementados

### 1. Codificação de Prüfer (`prufer_encode`)

O algoritmo recebe uma árvore e calcula sua sequência de Prüfer com tamanho `n - 2`.

Passos implementados:

1. É feita uma cópia da árvore original (`tree.copy()`), para evitar alterações no grafo de entrada.
2. Calcula-se o número de vértices `n` e inicializa-se um dicionário de graus (`deg`) com base na lista de adjacência da cópia.
3. Todas as folhas iniciais (`deg[v] == 1`) são inseridas em uma min-heap (`heapq`), permitindo sempre escolher a menor folha em `O(log n)`.
4. O laço principal executa exatamente `n - 2` iterações:
	- Remove-se da heap a menor folha (`leaf`).
	- Obtém-se seu único vizinho (`neighbor = t.adj_list[leaf][0]`).
	- Adiciona-se `neighbor` ao código de Prüfer.
	- Remove-se a aresta `(leaf, neighbor)` com `remove_edge`.
	- Atualizam-se os graus de `leaf` e `neighbor` no dicionário.
	- Se `neighbor` passar a ter grau 1, ele é inserido na heap como nova folha.
5. Após as `n - 2` remoções de folhas, a sequência acumulada é retornada.

Essa implementação mantém a definição clássica do código de Prüfer, mas com seleção eficiente da menor folha usando heap.

### 2. Decodificação de Prüfer (`prufer_decode`)

O algoritmo reconstrói a árvore a partir de um código de Prüfer.

Passos implementados:

1. Define-se `n = len(code) + 2` (quantidade de vértices da árvore).
2. Inicializa-se um vetor de graus com 1 para todos os vértices (`deg = [1] * n`).
3. Para cada valor `u` no código, incrementa-se `deg[u]`, pois cada ocorrência de `u` representa uma conexão adicional.
4. Todas as folhas atuais (`deg == 1`) são inseridas em uma min-heap (`heapq`), para sempre selecionar a menor folha.
5. Para cada `u` do código:
	- Remove-se da heap a menor folha `v`.
	- Adiciona-se a aresta `(u, v)` na árvore.
	- Decrementa-se `deg[u]`; se `deg[u]` virar 1, `u` passa a ser folha e entra na heap.
6. Ao final, restam duas folhas na heap; a última aresta entre elas é adicionada.

O uso de min-heap mantém a regra de menor rótulo em cada etapa da reconstrução.

### Métodos de apoio na classe `Graph`

- `add_edge(u, v)`: adiciona arestas em ambas as direções (grafo não direcionado), mantendo vizinhanças ordenadas.
- `remove_edge(u, v)`: remove a aresta dos dois lados e exclui vértices isolados da lista de adjacência.
- `binary_search(lst, target)`: encontra a posição de inserção ordenada dos vizinhos.
- `copy()`: cria uma cópia estrutural do grafo para uso seguro na codificação.

Com isso, o laboratório cobre tanto a transformação árvore -> código quanto código -> árvore, de forma consistente com vértices rotulados a partir de zero.

