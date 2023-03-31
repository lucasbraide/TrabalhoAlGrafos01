
with open('teste.txt') as f:
    entrada = f.readlines()

'''class Vertice:
    vizinhos = None
    grau = None

    def __init__(self, vizinhos):
        self.vizinhos = vizinhos
        self.grau = 0
        for i in len(vizinhos):
            self.grau += 1'''
class Grafo:
    nver = None
    arestas = None
    def __init__(self, nver, arestas):
        self.nver = nver
        self.arestas = arestas
    
    def printar_grafo(self):

        
                            

def calcular_dist(grafo, vertice):
    d = [None for i in range(grafo.nver())]
    d[vertice] = 0
    fila = []
    f.append(vertice)
    while len(f) > 0:
        aux = f.pop()
        for v in vizinhanca(aux):
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
    for i in arestas:
        if v in i:
            for aux in i:
                if aux != v:
                    viz.append(aux)
    return viz


n = conta_vertices(entrada)
arestas = monta_arestas(entrada, n)

grafo = Grafo(n, arestas)






