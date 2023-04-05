import sys
from collections import deque

'''with open('teste.txt') as f:
    entrada = f.readlines()'''


entrada = sys.stdin.readlines()

class Grafo:
    nver = None
    arestas = None
    def __init__(self, nver, lista_adj):
        self.nver = nver
        self.lista_adj = lista_adj

    def org_print_componentes(self):
        componentes = []
        lista_check = [False for i in range (self.nver)]
        for i in range(self.nver):
            if lista_check[i] == False:
                viz = vizinhanca(i+1, self.lista_adj)
                if len(viz) != 0:
                    componentes.append(viz)
                else:
                    componentes.append([i+1])
                for aux in viz:
                    lista_check[aux - 1] = True
        return componentes
            
    def print_componentes(self, componentes):
        for i in range (len(componentes)):
            print(" ".join([str(x) for x in componentes[i]]))

def conta_vertices(entrada):
    n = 0
    for i, line in enumerate(entrada):
        if i == 2:
            aux = line.split("=")
            n = int(aux[1])

    return n

def monta_arestas(entrada, nver):
    arestas = []
    for i, line in enumerate(entrada):
        if i >= 4:
            aux = line.split()
            a,b =  (int(aux[0]),int(aux[1]))
            arestas.append((a,b))

    return arestas

def build_adj_list(arestas, nver):
    adj_list = [[] for _ in range(nver)]
    for u, v in arestas:
        adj_list[u-1].append(v)
        adj_list[v-1].append(u)
    return adj_list


def vizinhanca(v, adj_list):
    visited = set()
    fila = []
    fila.append(v)
    while len(fila) != 0:
        u = fila.pop(0)
        visited.add(u)
        for vizinho in adj_list[u-1]:
            if vizinho not in visited:
                fila.append(vizinho)
                visited.add(vizinho)
    return sorted(visited)


nver = conta_vertices(entrada)
arestas = monta_arestas(entrada, nver)
lista_adj = build_adj_list(arestas, nver)
grafo = Grafo(nver, lista_adj)
componentes = grafo.org_print_componentes()
grafo.print_componentes(componentes)

