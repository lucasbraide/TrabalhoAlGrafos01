import sys
with open('teste.txt') as f:
    entrada = f.readlines()

class Grafo:
    nver = None
    arestas = None
    def __init__(self, nver, arestas):
        self.nver = nver
        self.arestas = arestas
    
    def org_print_grafo(self):
        componentes = []
        lista_check = [False for i in range (self.nver)]
        for i in range (self.nver):
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

def vizinhanca(v, arestas, lista_check):
    viz = []
    fila = []
    if v not in lista_check:
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
    else:
        return


n = conta_vertices(entrada)
arestas = monta_arestas(entrada, n)
grafo = Grafo(n, arestas)
componentes = grafo.org_print_grafo()
grafo.print_componentes(componentes)








