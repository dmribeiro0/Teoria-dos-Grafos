###############################################################################
# Daniel Monteiro Ribeiro                                                     #
# RA: 176231                                                                  #
# Laboratório 03 - Teoria dos Grafos                                          #
# Descrição: Dependência entre tarefas - Ordenação Topológica                 #
###############################################################################

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v: int):
        if v not in self.adj_list:
            self.adj_list[v] = []
    
    def add_arc(self, u: int, v: int):
        self.add_vertex(u)
        self.add_vertex(v)

        pos_v = self.binary_search(self.adj_list[u], v)
        if v not in self.adj_list[u]:
            self.adj_list[u].insert(pos_v, v)

    def get_size(self):
        m = 0
        for v in self.adj_list:
            m += len(self.adj_list[v])
        return m
    
    def get_order(self):
        return len(self.adj_list)

    def binary_search(self, lst: list, target: int) -> int:
        low, high = 0, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low