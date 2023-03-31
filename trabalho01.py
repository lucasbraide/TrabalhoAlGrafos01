import sys
'''with open('teste.txt') as f:
    entrada = f.readlines()
'''
entrada = sys.stdin.readlines()

class Grafo:
    nver = None
    arestas = None
    def __init__(self, nver, arestas):
        self.nver = nver
        self.arestas = arestas
    
    def org_print_grafo(self):
        componentes = []
        lista_check = [False for i in range (self.nver)]
        for i in range(0, self.nver):
            if lista_check[i] == False:
                viz = vizinhanca(i + 1, self.arestas)
                if len(viz) != 0:
                    componentes.append(viz)
                else:
                    componentes.append([i + 1])
                for aux in viz:
                    lista_check[aux - 1] = True
        return componentes
            
    def print_componentes(self, componentes):
        for i in range (len(componentes)):
            print(" ".join([str(x) for x in componentes[i]]))
                    

        
                            

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
    fila.append(v)
    while len(fila) != 0:
        u = fila.pop()
        for edge in arestas:
            if u in edge:
                for aux in edge:
                    if aux != u and aux not in viz:
                        fila.append(aux)
                        viz.append(aux) 
    viz.sort()
    return viz


n = conta_vertices(entrada)
arestas = monta_arestas(entrada, n)
grafo = Grafo(n, arestas)
componentes = grafo.org_print_grafo()
grafo.print_componentes(componentes)








