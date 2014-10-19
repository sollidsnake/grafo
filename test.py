from grafo import Grafo

grafo = Grafo()
grafo.addAresta('a')
grafo.addAresta('b')
grafo.addAresta('c')
grafo.addVertice('1')
grafo.addVertice('2')
grafo.addVertice('3')
grafo.addVertice('4')
grafo.addConexao('1', 'a', '2')
grafo.addConexao('2', 'b', '3')
grafo.addConexao('3', 'c', '1')

print(grafo.procuraLigacao('1', '3')[1])
