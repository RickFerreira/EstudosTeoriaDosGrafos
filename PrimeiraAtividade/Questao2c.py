# utilizando a biblioteca igrafh e a dependencia cairo
from igraph import *

# criando o grafo
questao2c = Graph.Tree(5, 5)

#estilo do grafo
visual_style = {}
#cor dos vertices
visual_style["vertex_color"] = "cyan"
#nome dos vertices
visual_style["vertex_label"] = ["A", "B", "C", "D", "E"]
#tamanho da imagem gerada
visual_style["bbox"] = (300, 300)

# mostrando o grafo
print(questao2c)
# gerando imagem do grafo
plot(questao2c, **visual_style)


