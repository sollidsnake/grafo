from grafo import Grafo
import pdb

grafo = Grafo()

grafo.addVertice('1')
grafo.addVertice('2')
grafo.addVertice('3')

grafo.addAresta('a')
grafo.addAresta('b')
grafo.addAresta('c')

grafo.addConexao('1', 'a', '2')
grafo.addConexao('1', 'b', '3')
grafo.addConexao('3', 'c', '3')

grafo.conexoes = {('2', 'd', '1'): 1, ('1', 'b', '3'): 1, ('1', 'a', '2'): 1, ('3', 'c', '3'): 1}

grafo.setDirecionado(True)

print(grafo.getGrau('1'))
