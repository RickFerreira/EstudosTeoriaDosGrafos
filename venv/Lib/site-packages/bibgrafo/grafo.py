class GrafoIF():

    SEPARADOR_ARESTA = '-'

    def verticeValido(self, vertice='') -> bool:
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        O caractere separador serve para prover uma representação em string do grafo e pode ser alterado com o método setCaractereSeparador().
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        pass

    def arestaValida(self, aresta=tuple()) -> bool:
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um tupla com o formato (a, b), onde:
        a é um string de aresta que é o nome de um vértice adjacente à aresta.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''
        pass

    def existeVertice(self, vertice='') -> bool:
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        pass

    def existeRotuloAresta(self, aresta='') -> bool:
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        pass

    def getCaractereSeparador(self) -> str:
        '''
        Retorna o caractere separador.
        :return: o caractere separador.
        '''
        pass

    def setCaractereSeparador(self, caractere=''):
        '''
        Altera o caractere separador.
        :param: o caractere separador.
        '''
        pass

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        pass

    def adicionaAresta(self, nome='', a=tuple()):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param a: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        pass

    def __str__(self) -> str:
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato v1-v2.
        Em que v1 é o primeiro vértice, v2 é o segundo vértice e o traço (-) é uma representação do caractere separador.
        :return: Uma string que representa o grafo
        '''
        pass































