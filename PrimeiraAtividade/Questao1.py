# utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

# criando o grafo
questao1 = Graph()

# adicionando a quantidade de vertices(bolas)
questao1.add_vertices(7)

# adicionando as ligações(arestas) entre cada vertice
questao1.add_edges([(0, 1), (1, 2), (2, 3), (3, 4), (2, 4), (4, 5), (5, 6)])

#estilo do grafo
visual_style = {}
#cor dos vertices
visual_style["vertex_color"] = "cyan"
#nome dos vertices
visual_style["vertex_label"] = ["1", "2", "3", "4", "5", "6", "7"]
#tamanho da imagem gerada
visual_style["bbox"] = (400, 300)

# mostrando o grafo
print(questao1)
# gerando imagem do grafo
plot(questao1, **visual_style)
