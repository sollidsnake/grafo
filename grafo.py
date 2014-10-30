import pdb

class Grafo(object):
    vertices = []
    arestas = []
    conexoes = {}
    lacos = []
    matrizIncidencia = {}

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

    def addConexao(self, v1, aresta, v2, peso = 1, direcionado=False):
        self.conexoes[v1, aresta, v2] = peso
        if direcionado:
            self.conexoes[v2, aresta, v1] = peso * -1
        else:
            self.conexoes[v2, aresta, v1] = peso

        self.matrizIncidencia[v1, aresta] = peso
        self.matrizIncidencia[v2, aresta] = peso

    def getConexoes(self):
        return self.conexoes

    def getLaco(self):
        for v1, a, v2 in self.conexoes:
            peso = self.conexoes[v1, a, v2]
            if v1 == v2 and peso != 0:
                return True

        return False

    def procuraCaminho(self, v1, v2, nosVisitados=[]):
        ligacoes = []

        for v3, a, v4 in self.conexoes:
            peso = self.conexoes[v3, a, v4]
            if peso < 0: continue
            if v1 == v3:
                if v4 == v2:
                    return True

                if v4 not in nosVisitados:
                    ligacoes.append(v4)
                    nosVisitados.append(v4)

        for ligacao in ligacoes:
            encontrado = self.procuraCaminho(ligacao, v2, nosVisitados)
            if encontrado: return True

        return False

    def procuraArestaParalela(self):
        ligacoes = {}
        for v3, a, v4 in self.conexoes:
            if (v3, v4) not in ligacoes.keys():
                ligacoes[v3, v4] = 1
            else: return True

        return False


    def procuraVerticeIsolado(self):

        for v in self.vertices:
            for v1, a, v2 in self.conexoes:
                isolado = True
                if v1 == v:
                    isolado = False
                    break

        if isolado: return True

        return False


    def getOrdem(self):
        return len(self.vertices)

    def getGrau(self, v):
        grau = 0
        for v1, a, v2 in self.conexoes:
            peso = self.conexoes[v1, a, v2]
            if v1 == v and peso > 0: grau += 1

        return grau

    def getTodosGraus(self):
        graus = {}
        for v in self.vertices:
            graus[v] = self.getGrau(v)

        return graus
