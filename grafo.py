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

    def setDirecionado(self, direcionado):
        if direcionado == True:
            for v1, a, v2 in self.conexoes:
                peso = self.conexoes[v1, a, v2]
                if peso > 0:
                    pesoReverso = peso * -1
                    self.conexoes[v2, a, v1] = pesoReverso

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

    def existeLaco(self):
        for v1, a, v2 in self.conexoes:
            peso = self.conexoes[v1, a, v2]
            if v1 == v2 and peso != 0:
                return True

        return False

    def existeCaminho(self, v1, v2, nosVisitados=[]):
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
            encontrado = self.existeCaminho(ligacao, v2, nosVisitados)
            if encontrado: return True

        return False

    def existeArestaParalela(self):
        ligacoes = {}
        for v3, a, v4 in self.conexoes:
            if (v3, v4) not in ligacoes.keys():
                ligacoes[v3, v4] = 1
            else: return True

        return False


    def existeVerticeIsolado(self):

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

    def getAdjacentes(self, v):
        adjacentes = []

        for v1, a, v2 in self.conexoes:
            if v1 == v:
                adjacentes.append((a, v2))

        return adjacentes

    def getGrafoPadrao(self):
        grafo = {}

        for v in self.vertices:
            grafo[v] = []
            for arestaAdj, vertAdj in self.getAdjacentes(v):
                grafo[v].append(vertAdj)

        return grafo

    def existeCiclo(self, destino):

        # caminhosTentados = []
        # caminhoAtual = []
        arestasVisitadas = []
        vertList = [destino]
        # vertBlackList = []
        adjacentesList = {}
        vertNumTentativas = {}

        # se tem laco existe ciclo
        if self.existeLaco(): return True

        for v in self.vertices:
            adjacentes = self.getAdjacentes(v)
            adjacentesList[v] = []
            for arestaAdj, vertAdj in adjacentes:
                adjacentesList[v].append(vertAdj)

        def buscaCiclo(vertice):
            print(vertice)
            if vertice == destino and len(vertList) > 2: return True
            adjacentes = self.getAdjacentes(vertice)
            for arestaAdj, vertAdj in adjacentes:
                semCaminho = False
                if arestaAdj in arestasVisitadas:
                    semCaminho = True
                    continue

                # try: vertNumTentativas[vertice] += 1
                # except: vertNumTentativas[vertice] = 1

                vertList.append(vertAdj)
                arestasVisitadas.append(arestaAdj)
                return buscaCiclo(vertAdj)

            if semCaminho:
                if len(vertList) > 1:
                    vertList.pop()

                vertTmp = vertList[len(vertList)-1]

                try: vertNumTentativas[vertTmp] += 1 
                except: vertNumTentativas[vertTmp] = 1 

                if vertNumTentativas[vertTmp] > len(adjacentesList[vertTmp]):
                    return False

                return buscaCiclo(vertTmp)
            return False

        return buscaCiclo(destino)
