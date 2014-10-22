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

    def procuraLigacao(self, v1, v2):
        for v3, a, v4 in self.conexoes:
            keys = (v3, a, v4)
            if v1 == v3 and v2 == v4 and keys in self.conexoes and self.conexoes[keys] != 0:
                # retorna aresta e peso
                return a, self.conexoes[keys]

        return False

    def addConexao(self, v1, aresta, v2, peso = 1):
        self.conexoes[(v1, aresta, v2)] = peso
        self.conexoes[(v2, aresta, v1)] = peso

    def getConexoes(self):
        return self.conexoes

    def getLaco(self):
        for v1, a, v2 in self.conexoes:
            peso = self.conexoes[(v1, a, v2)]
            if v1 == v2 and peso != 0:
                l = 'Aresta '+a+' em: '+v1
                self.lacos.append(l)
        return self.lacos
