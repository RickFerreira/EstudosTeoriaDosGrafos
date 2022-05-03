from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia


paraiba = GrafoListaAdjacencia(["J", "C", "E", "P", "M", "T", "Z"])

paraiba.adicionaAresta("a1", "J", "C")
paraiba.adicionaAresta("a2", "C", "E")
paraiba.adicionaAresta("a3", "C", "E")
paraiba.adicionaAresta("a4", "C", "P")
paraiba.adicionaAresta("a5", "C", "P")
paraiba.adicionaAresta("a6", "C", "M")
paraiba.adicionaAresta("a7", "C", "T")
paraiba.adicionaAresta("a8", "M", "T")
paraiba.adicionaAresta("a9", "T", "Z")



print(paraiba)
