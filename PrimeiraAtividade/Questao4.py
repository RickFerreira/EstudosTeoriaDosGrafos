# utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

# criando o grafo
questao4 = Graph()

# adicionando a quantidade de vertices(bolas)
questao4.add_vertices(4)

# adicionando as ligações(arestas) entre cada vertice
questao4.add_edges([(0, 1),
                    (1, 2), (1, 3),
                    (2, 2), (3, 2)])

#estilo do grafo
visual_style = {}
#cor dos vertices
visual_style["vertex_color"] = "cyan"
#nome dos vertices
visual_style["vertex_label"] = ["A", "B", "C", "D"]
#tamanho da imagem gerada
visual_style["bbox"] = (300, 300)

# mostrando o grafo
print(questao4)
# gerando imagem do grafo
plot(questao4, **visual_style)
