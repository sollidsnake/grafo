import pdb

from copy import deepcopy

class Grafo(object):
    vertices = []
    arestas = []
    conexoes = {}
    lacos = []
    matrizIncidencia = {}
    isDirecionado = False

    def __init__(self, matriz=None):
        if matriz:
            self.matriz = matriz

    def getVertices(self):
        return self.vertices

    def removeVertice(self, v):
        self.vertices.remove(v)

        conexoesTmp = deepcopy(self.conexoes)

        for v1, a, v2 in conexoesTmp:
            if v1 == v or v2 == v:
                self.conexoes.pop((v1, a, v2))

    def removeAresta(self, aresta):
        self.arestas.remove(aresta)

        conexoesTmp = deepcopy(self.conexoes)

        for v1, a, v2 in conexoesTmp:
            if a == aresta:
                self.conexoes.pop((v1, a, v2))
    
        
    def removeConexao(self, aresta):
        conexoesTmp = deepcopy(self.conexoes)
        for v1, a, v2 in conexoesTmp:
            if a == aresta:
                self.conexoes.pop((v1, a, v2))

    def addVertice(self, v):
        self.vertices.append(v)

    def addAresta(self, a):
        self.arestas.append(a)

    def procuraLigacao(self, v1, v2):
        for v3, a, v4 in self.conexoesComDirecao:
            keys = (v3, a, v4)
            if v1 == v3 and v2 == v4 and keys in self.conexoesComDirecao and self.conexoesComDirecao[keys] != 0:
                # retorna aresta e peso
                return a, self.conexoes[keys]

        return False

    def setDirecionado(self, direcionado):
        self.conexoesComDirecao = deepcopy(self.conexoes)

        
        if direcionado == True:

            for v1, a, v2 in self.conexoes:
                if v1 == v2: continue
                peso = self.conexoes[v1, a, v2]
                pesoReverso = peso * -1
                self.conexoesComDirecao[v2, a, v1] = pesoReverso

            self.isDirecionado = True

        else:
            for v1, a, v2 in self.conexoes:
                peso = self.conexoes[v1, a, v2]
                self.conexoesComDirecao[v2, a, v1] = peso

            self.isDirecionado = False
                    

    def addConexao(self, v1, aresta, v2, peso = 1, direcionado=False):
        self.conexoes[v1, aresta, v2] = peso

        self.matrizIncidencia[v1, aresta] = peso
        self.matrizIncidencia[v2, aresta] = peso

    def getConexoes(self):
        return self.conexoesComDirecao

    def existeLaco(self):
        for v1, a, v2 in self.conexoesComDirecao:
            peso = self.conexoesComDirecao[v1, a, v2]
            if v1 == v2 and peso != 0:
                return True

        return False

    def getLaco(self):
         for v1, a, v2 in self.conexoes:
             peso = self.conexoes[(v1, a, v2)]
             if v1 == v2 and peso != 0:
                l = 'Aresta '+a+' em: '+v1
                self.lacos.append(l)
       return self.lacos

    def getTodasAdjacencias(self):
        adjacencias = {}
        for v in self.vertices:
            adjacencias[v] = self.getAdjacentes(v)

        return adjacencias

    def existeCaminho(self, v1, v2, nosVisitados=[]):
        ligacoes = []

        for v3, a, v4 in self.conexoesComDirecao:
            peso = self.conexoesComDirecao[v3, a, v4]
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
        for v3, a, v4 in self.conexoesComDirecao:
            if (v3, v4) not in ligacoes.keys():
                ligacoes[v3, v4] = 1
            else: return True

        return False


    def existeVerticeIsolado(self):

        if not self.conexoesComDirecao:
            return False

        for v in self.vertices:
            for v1, a, v2 in self.conexoesComDirecao:
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
        grauReceptivo = 0

        for v1, a, v2 in self.conexoesComDirecao:
            peso = self.conexoesComDirecao[v1, a, v2]
            if v1 == v:
                if peso > 0:
                    grau += 1
                else:
                    grauReceptivo += 1
                
        if self.isDirecionado:
            return (grau, grauReceptivo)

        return grau

    def getTodosGraus(self):
        graus = {}
        for v in self.vertices:
            graus[v] = self.getGrau(v)

        return graus

    def getAdjacentes(self, v):
        adjacentes = []

        for v1, a, v2 in self.conexoesComDirecao:
            peso = self.conexoesComDirecao[v1, a, v2]
            if peso < 0: continue
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

    def getCiclos(self):
        ciclos = []
        for v in self.vertices:
            if self.existeCicloParaNo(v):
                ciclos.append(v)

        return ciclos

    def temLaco(self, v):
        for v1, a, v2 in self.conexoes:
            if v1 == v2 and v == v1:
                return True

        return False

    def isConexo(self):
        for v1 in self.vertices:
            for v2 in self.vertices:
                if self.existeCaminho(v1, v2, []) == False:
                    return False

        return True

    def existeCicloParaNo(self, destino):
        """ Verifica se existe ciclo para o vertice passado por parametro """

        arestasVisitadas = []
        caminhoPercorrido = [destino]
        adjacentesList = {}
        vertNumTentativas = {}

        # se tem laco existe ciclo
        if self.temLaco(destino): return True

        for v in self.vertices:
            # monta indice de adjacentes para os nos
            adjacentes = self.getAdjacentes(v)
            adjacentesList[v] = []
            for arestaAdj, vertAdj in adjacentes:
                adjacentesList[v].append(vertAdj)

        # funcao de busca recursiva
        def buscaCiclo(vertice):
            if vertice == destino and len(caminhoPercorrido) > 2: return True
            adjacentes = self.getAdjacentes(vertice)
            semCaminho = False
            for arestaAdj, vertAdj in adjacentes:
                semCaminho = False
                if arestaAdj in arestasVisitadas:
                    semCaminho = True
                    continue

                caminhoPercorrido.append(vertAdj)
                arestasVisitadas.append(arestaAdj)
                return buscaCiclo(vertAdj)

            if semCaminho or len(adjacentes) == 0:
                if len(caminhoPercorrido) > 1:
                    caminhoPercorrido.pop()

                vertTmp = caminhoPercorrido[len(caminhoPercorrido)-1]

                try: vertNumTentativas[vertTmp] += 1 
                except: vertNumTentativas[vertTmp] = 1 

                if vertNumTentativas[vertTmp] > len(adjacentesList[vertTmp]):
                    return False

                return buscaCiclo(vertTmp)
            return False

        return buscaCiclo(destino)
