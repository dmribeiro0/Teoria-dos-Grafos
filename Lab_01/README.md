# Teoria dos Grafos 2026 (1S) — Laboratório 1

---

## Descrição

Implemente uma classe `Graph` que represente um grafo. Para isso, use um dicionário para implementar uma lista de adjacência. As operações de inserção e busca na lista de adjacência de cada vértice devem ser feitas em $O(log\,n)$, para $n$ sendo o tamanho da lista de adjacência. Ou seja, as listas de adjacência devem ser mantidas ordenadas lexicograficamente a cada inserção. Exemplo: se $(v0, v3)$ e $(v0, v1)$ são arestas, então a lista de adjacência de $v0$ é `{v0: [v1, v3], ...}` e não `{v0: [v3, v1], ...}`.

Soluções que violem as condições do exercício não serão aceitas.

## Entrada

A entrada consiste em $m + 1$ linhas, cada uma contendo um par de vértices separados por um espaço. Cada par representa uma aresta a ser inserida no grafo. A última linha $(m + 1)$ contém uma aresta a ser consultada no grafo.

## Saída

```text
Order: <numero de vertices no grafo>
Size: <numero de arestas no grafo>
Min degree: <grau minimo de um vertice no grafo>
Max degree: <grau maximo de um vertice no grafo>
Average degree: <grau medio dos vertices no grafo>
Degree list: <lista dos graus dos vertices no grafo>
rotulo do vertice: <lista de vizinhos do vertice no grafo>
<True ou False>
```

As $n$ linhas que antecedem a linha com `True` ou `False` da saída são compostas pelos vértices do grafo em ordem e sua respectiva lista de adjacência. Aqui é permitido o uso da função `sorted` para ordenar os vértices, mas não as suas listas de adjacências. O mesmo se aplica à linha `Degree list`, que obedecerá à ordem lexicográfica. Para o grau médio `Average degree`, use apenas uma casa decimal.

## Exemplo de entrada e saída

```text
Exemplo de entrada
3
v0 v3
v1 v2
v2 v3
v3 v0

Exemplo de saída
Order: 4
Size: 3
Min degree: 1
Max degree: 2
Average degree: 1.5
Degree list: [1, 1, 2, 2]
v0: ['v3']
v1: ['v2']
v2: ['v1', 'v3']
v3: ['v0', 'v2']
True
```

