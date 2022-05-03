#Primeiro grafo utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

#São gerados nesse caso um grafo com 15 vertices
#As arestas são aleatorias também e
#Pode ir de 0 até 3 ligações para cada vertice
grafoAleatorio = Graph.GRG(15, 0.3)
#Todas as vezes um grafo diferente será feito
plot(grafoAleatorio)

