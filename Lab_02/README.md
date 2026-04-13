# Teoria dos Grafos 2026 (1S) — Laboratório 2

---

## Descrição

Seja $G$ um grafo. O grafo é inicialmente fornecido por meio da quantidade de arestas seguida pela sua lista de arestas. Seu objetivo é implementar uma função que, recebendo somente a matriz de adjacência de $G$ como parâmetro, determine o número de ciclos de comprimento exatamente quatro em $G$.

Um ciclo de comprimento quatro é definido como uma sequência de quatro vértices distintos $(v_0, v_1, v_2, v_3, v_0)$ tal que cada par consecutivo de vértices, incluindo $(v_3, v_0)$, é conectado por uma aresta em $G$. Ciclos que diferem apenas pela escolha do vértice inicial ou pelo sentido de travessia, isto é, considerando rotações ou inversões, não devem ser contados como distintos.

Para realizar essa tarefa, será necessário, inicialmente, estender a implementação da classe `Graph`, criada no Laboratório 1, com um método adicional responsável por transformar a lista de adjacência em uma matriz de adjacência. Essa matriz deve ser construída seguindo a ordenação lexicográfica dos rótulos dos vértices. Não é permitido converter a matriz de volta para outra representação dentro da função que realiza a contagem de ciclos.

O algoritmo implementado deve basear-se unicamente nos métodos e técnicas formalmente discutidos em sala de aula até o presente momento da disciplina. Soluções que empreguem algoritmos, estratégias, bibliotecas ou técnicas que não tenham sido formalmente introduzidas até aqui, ainda que sabidamente corretas ou eficientes, serão consideradas inválidas. Não é necessária otimização especial, contanto que a execução não ultrapasse o tempo limite definido no Judge. Violações a qualquer uma das condições, mesmo que aparentem vantagens práticas, invalidam completamente a submissão.

