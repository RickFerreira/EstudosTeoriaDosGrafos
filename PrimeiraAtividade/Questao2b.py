# utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

# criando o grafo
questao2a = Graph()

# adicionando a quantidade de vertices(bolas)
questao2a.add_vertices(4)

# adicionando as ligações(arestas) entre cada vertice
questao2a.add_edges([(0, 0),
                     (0, 1), (1, 0),
                     (1, 2), (2, 3), (3, 1),
                     (3, 0)])

#estilo do grafo
visual_style = {}
#cor dos vertices
visual_style["vertex_color"] = "cyan"
#nome dos vertices
visual_style["vertex_label"] = ["A", "B", "C", "D"]
#tamanho da imagem gerada
visual_style["bbox"] = (300, 300)

# mostrando o grafo
print(questao2a)
# gerando imagem do grafo
plot(questao2a, **visual_style)
