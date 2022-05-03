# utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

# criando o grafo
questao2a = Graph()

# adicionando a quantidade de vertices(bolas)
questao2a.add_vertices(3)

# adicionando as ligações(arestas) entre cada vertice
questao2a.add_edges([(0, 1), (1, 2), (2, 0)])

#estilo do grafo
visual_style = {}
#cor dos vertices
visual_style["vertex_color"] = "cyan"
#nome dos vertices
visual_style["vertex_label"] = ["A", "B", "C"]
#tamanho da imagem gerada
visual_style["bbox"] = (200, 200)

# mostrando o grafo
print(questao2a)
# gerando imagem do grafo
plot(questao2a, **visual_style)
