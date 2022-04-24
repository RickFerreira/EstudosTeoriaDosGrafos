# utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

# criando o grafo
questao4c = Graph()

# adicionando a quantidade de vertices(bolas)
questao4c.add_vertices(5)

# adicionando as ligações(arestas) entre cada vertice
questao4c.add_edges([(0, 1), (0, 2), (2, 3), (2, 3), (3, 4), (4, 4)])

#estilo do grafo
visual_style = {}
#cor dos vertices
visual_style["vertex_color"] = "cyan"
#nome dos vertices
visual_style["vertex_label"] = ["1", "2", "3", "4", "5"]
#tamanho da imagem gerada
visual_style["bbox"] = (600, 600)

# mostrando o grafo
print(questao4c)
# gerando imagem do grafo
plot(questao4c, **visual_style)
