#Primeiro grafo utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

#criando o grafo
helloGrafo = Graph()

#adicionando a quantidade de vertices(bolas)
helloGrafo.add_vertices(5)

#adicionando as ligações(arestas) entre cada vertice
helloGrafo.add_edges([(0,1),(1,2),(2,3),(3,4),(4,0),(0,3),(0,2)])

#gerando imagem do grafo
plot(helloGrafo)

