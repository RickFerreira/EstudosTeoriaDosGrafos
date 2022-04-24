# utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

# criando o grafo
questao3 = Graph()

# adicionando a quantidade de vertices(bolas)
questao3.add_vertices(6)

# adicionando as ligações(arestas) entre cada vertice
questao3.add_edges([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                    (1, 2), (1, 3), (1, 4), (1, 5),
                    (2, 3), (2, 4), (2, 5),
                    (3, 4), (3, 5),
                    (4, 5)])

#estilo do grafo
visual_style = {}
#cor dos vertices
visual_style["vertex_color"] = "cyan"
#nome dos vertices
visual_style["vertex_label"] = ["A", "B", "C", "D", "E", "F"]
#tamanho da imagem gerada
visual_style["bbox"] = (300, 300)

# mostrando o grafo
print(questao3)
# gerando imagem do grafo
plot(questao3, **visual_style)


