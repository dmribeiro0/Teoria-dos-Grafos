# Teoria dos Grafos 2026 (1S) — Laboratório 2

---

## Descrição

Seja $G$ um grafo. O grafo é inicialmente fornecido por meio da quantidade de arestas seguida pela sua lista de arestas. Seu objetivo é implementar uma função que, recebendo somente a matriz de adjacência de $G$ como parâmetro, determine o número de ciclos de comprimento exatamente quatro em $G$.

Um ciclo de comprimento quatro é definido como uma sequência de quatro vértices distintos $(v_0, v_1, v_2, v_3, v_0)$ tal que cada par consecutivo de vértices, incluindo $(v_3, v_0)$, é conectado por uma aresta em $G$. Ciclos que diferem apenas pela escolha do vértice inicial ou pelo sentido de travessia, isto é, considerando rotações ou inversões, não devem ser contados como distintos.

Para realizar essa tarefa, será necessário, inicialmente, estender a implementação da classe `Graph`, criada no Laboratório 1, com um método adicional responsável por transformar a lista de adjacência em uma matriz de adjacência. Essa matriz deve ser construída seguindo a ordenação lexicográfica dos rótulos dos vértices. Não é permitido converter a matriz de volta para outra representação dentro da função que realiza a contagem de ciclos.

O algoritmo implementado deve basear-se unicamente nos métodos e técnicas formalmente discutidos em sala de aula até o presente momento da disciplina. Soluções que empreguem algoritmos, estratégias, bibliotecas ou técnicas que não tenham sido formalmente introduzidas até aqui, ainda que sabidamente corretas ou eficientes, serão consideradas inválidas. Não é necessária otimização especial, contanto que a execução não ultrapasse o tempo limite definido no Judge. Violações a qualquer uma das condições, mesmo que aparentem vantagens práticas, invalidam completamente a submissão.

---

## Solução

### Proposição

Se $G$ é um grafo de ordem 4 e o grau mínimo de $G$ é maior ou igual a 2, então $G$ contém um ciclo de tamanho 4.

---

### Demonstração

Seja $G$ um grafo com 4 vértices e grau mínimo maior ou igual a 2. Isso significa que cada vértice de $G$ possui pelo menos dois vizinhos.

A partir disso, podemos analisar as possíveis sequências de graus dos vértices. Como cada vértice tem grau pelo menos 2 e no máximo 3, existem três casos possíveis:

1. todos os vértices com grau 2;
2. dois vértices com grau 2 e dois com grau 3;
3. todos os vértices com grau 3.

Pelo Lema do Aperto de Mãos, a soma dos graus dos vértices é igual ao dobro do número de arestas do grafo. Assim:

- se todos os graus são 2, a soma é 8, então o grafo tem 4 arestas;
- se dois vértices têm grau 2 e dois têm grau 3, a soma é 10, então o grafo tem 5 arestas;
- se todos os vértices têm grau 3, a soma é 12, então o grafo tem 6 arestas.

Agora analisamos cada caso.

### Caso 1: todos os vértices com grau 2

Nesse caso, o grafo é necessariamente um ciclo com 4 vértices, isto é, o $C_4$. Portanto, ele já contém um ciclo de tamanho 4.

### Caso 2: dois vértices com grau 2 e dois com grau 3

Nesse caso, o grafo pode ser visto como um $C_4$ com a adição de uma aresta extra, isto é, uma diagonal. Como adicionar uma aresta não remove ciclos existentes, o ciclo de tamanho 4 continua presente no grafo.

### Caso 3: todos os vértices com grau 3

Nesse caso, o grafo é o grafo completo com 4 vértices, isto é, o $K_4$. Nesse grafo, todo par de vértices é adjacente, então é sempre possível escolher quatro vértices e percorrê-los em ciclo, formando um ciclo de tamanho 4.

### Conclusão

Em todos os casos possíveis, o grafo $G$ contém um ciclo de comprimento 4.

### Implementação
A implementação da função `is_there_a_cycle` foi baseada na proposição e demonstração acima. A função calcula a soma dos graus dos quatro vértices selecionados e, com base nessa soma, determina se eles formam um ciclo de comprimento 4, quantos ciclos formam ou se não formam nenhum ciclo.
A função `count_C4` itera sobre todas as combinações de quatro vértices distintos e utiliza a função `is_there_a_cycle` para contar quantos ciclos de comprimento 4 existem no grafo representado pela matriz de adjacência.
Contudo, o método de checar todas as combinações de quatro vértices é ineficiente para grafos grandes, já que tem uma complexidade de tempo de $O(n^4)$.
