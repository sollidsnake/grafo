from grafo import Grafo

grafo = Grafo()

grafo.addVertice('1')
grafo.addVertice('2')
grafo.addVertice('3')
grafo.addVertice('4')
grafo.addVertice('5')

grafo.addAresta('a')
grafo.addAresta('b')
grafo.addAresta('c')
grafo.addAresta('d')
grafo.addAresta('e')

grafo.addConexao('1', 'a', '2')
grafo.addConexao('1', 'b', '5')
grafo.addConexao('2', 'c', '5')
grafo.addConexao('1', 'd', '3')
grafo.addConexao('5', 'e', '4')

print(grafo.existeCiclo('4'))
