#Primeiro grafo utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

#gerando um grafo de arvore com 31 vertices
#cada vertice tem dois filhos e um pai até completar os 31
grafoArvore = Graph.Tree(31, 2)

plot(grafoArvore)

