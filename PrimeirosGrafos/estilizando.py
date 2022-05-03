# importando a biblioteca
from igraph import *

# gerando o grafo
grafoEstilizado = Graph(directed=False)
# criando as vertices
grafoEstilizado.add_vertices(6)
# criando as arestas
grafoEstilizado.add_edges([(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (5, 3)])
# criando as larguras de cada aresta na ordem respectiva criada anteriormente
grafoEstilizado.es['weight'] = [1, 12, 2, 3, 4, 1]

# criando o estilo dos vertices
visual_style = {}
# adcionando cada letra na ordem respectiva criada anteriormente
visual_style["vertex_label"] = ["a", "b", "c", "d", "e", "f"]
# escolhendo a largura e dizendo que vai ser igual a determinada anteriormente
visual_style["edge_width"] = grafoEstilizado.es['weight']
# determinado o tamanho da imagem que vai gerar em px
visual_style["bbox"] = (300, 300)

# gerando imagem com o estilo completo que foi feito
plot(grafoEstilizado, **visual_style)
