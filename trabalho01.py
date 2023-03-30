import sys


with open('0.in') as f:
    entrada = f.readines()


class Grafo:
    nver = None
    arestas = None
    def __init__(self, nver, arestas):
        self.nver = nver
        self.arestas = arestas


def conta_vertices(entrada):
    n = 0
    for i, line in enumerate(entrada):
        if i == 2:
            aux = line.split("=")
            n = aux[1]

    return n

def monta_arestas(entrada, nver):
    arestas = []
    for i, line in enumerate(entrada):
        if i >= 4:
            aux = line.split()
            (a,b) =  (aux[0],aux[1])
            arestas.append((a,b))

    return arestas

n = conta_vertices(entrada)
arestas = monta_arestas(entrada, n)

grafo = Grafo(n, arestas)

print(grafo.arestas)
print(grafo.nver)




