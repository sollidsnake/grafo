class Grafo(object):
    vertices = []
    arestas = []
    conexoes = {}
    lacos = []

    def __init__(self, matriz=None):
        if matriz:
            self.matriz = matriz

    def addVertice(self, v):
        self.vertices.append(v)

    def addAresta(self, a):
        self.arestas.append(a)

    def addConexao(self, v1, aresta, v2, peso = 1):
        self.conexoes[(v1, aresta, v2)] = peso

    def getConexoes(self):
        return self.conexoes

    def procuraLaco(self):
        for v1, a, v2 in self.conexoes:
            peso = self.conexoes[(v1, a, v2)]
            if v1 == v2 and peso != 0:
                return True

        return False
