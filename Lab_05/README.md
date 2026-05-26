# Laboratório 05 - Teoria dos Grafos

## Descrição da atividade

O objetivo deste laboratório é resolver um problema de **caminho mínimo** em um grafo dirigido e ponderado. A aplicação recebe uma rede de rotas entre vértices, identifica quais centros de distribuição possuem o produto em estoque e determina qual deles oferece o melhor caminho até o cliente.

## Solução implementada

A solução foi desenvolvida no arquivo `lab05.py` e segue a ideia de transformar o problema em um caso de **single-destination shortest path**. Como o destino é fixo, o grafo original é invertido e o algoritmo de Dijkstra é executado a partir do vértice do cliente no grafo reverso.

### Estrutura do grafo

O grafo é armazenado com:

- lista de adjacência para os vértices;
- dicionário para os pesos das arestas;
- inserção ordenada dos vizinhos com busca binária.

### Etapas do algoritmo

1. Leitura das arestas do grafo com seus respectivos pesos.
2. Leitura dos centros de distribuição e da informação de estoque.
3. Leitura do vértice cliente.
4. Construção do grafo reverso.
5. Execução do Dijkstra a partir do cliente no grafo invertido.
6. Verificação dos centros que possuem produto e que alcançam o cliente.
7. Reconstituição do caminho com os predecessores.
8. Seleção da menor rota encontrada.

### Critério de escolha da rota

Entre todos os centros que possuem produto e conseguem chegar ao cliente, o programa escolhe o caminho com menor peso total. O tempo da rota é calculado com `floor(peso_total / 100)`.

## Saída do programa

Se existir ao menos uma rota válida, o programa imprime:

- o vértice do centro de distribuição escolhido;
- o tempo estimado da rota;
- o caminho completo até o cliente.

Caso não exista rota disponível ou não haja produto em estoque, o programa informa essa situação ao usuário.

