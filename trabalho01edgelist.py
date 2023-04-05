import sys

with open('teste.txt') as f:
    entrada = f.readlines()

'''entrada = sys.stdin.readlines()'''

class Grafo:
    nver = None
    arestas = None
    def __init__(self, nver, arestas):
        self.nver = nver
        self.arestas = arestas
    
    def org_print_grafo(self):
        componentes = []
        lista_check = []
        for i in range(1, self.nver + 1):
            if i not in lista_check:
                if len(vizinhanca(i, self.arestas)) != 0:
                    componentes.append(vizinhanca(i, self.arestas))
                else:
                    componentes.append([i])
                for aux in vizinhanca(i,self.arestas):
                    lista_check.append(aux)
        return componentes
            
    def print_componentes(self, componentes):
        for i in range (len(componentes)):
            print(" ".join([str(x) for x in componentes[i]]))



def build_adj_list(edges, num_vertices):
    adj_list = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


                    

def calcular_dist(grafo, vertice):
    d = [None for i in range(0, grafo.nver)]
    d[vertice] = 0
    f = []
    f.append(vertice)
    while len(f) > 0:
        aux = f.pop()
        for v in vizinhanca(aux, grafo.arestas):
            if d[v] == None:
                d[v] = d[aux] + 1
                f.append(v)

    return d


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
            arestas.append([a,b])

    return arestas

def vizinhanca(v, arestas):
    viz = []
    fila = []
    visitado = set()
    fila.append(v)
    while len(fila) != 0:
        u = fila.pop()
        for edge in arestas:
            if u in edge:
                for aux in edge:
                    if aux != u and aux not in visitado:
                        visitado.add(aux)
                        fila.append(aux)
                        viz.append(aux) 

    viz.sort()
    return viz


n = conta_vertices(entrada)
arestas = monta_arestas(entrada, n)
grafo = Grafo(n, arestas)
componentes = grafo.org_print_grafo()
grafo.print_componentes(componentes)







