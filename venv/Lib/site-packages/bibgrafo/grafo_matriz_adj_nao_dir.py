from bibgrafo.grafo import GrafoIF
from bibgrafo.aresta import Aresta
from bibgrafo.grafo_exceptions import *

class GrafoMatrizAdjacenciaNaoDirecionado(GrafoIF):

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not(GrafoMatrizAdjacenciaNaoDirecionado.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')


        self.N = list(V)

        if M == []:
            self.M = list()
            for k in range(len(V)):
                self.M.append(list())
                for l in range(len(V)):
                    if k>l:
                        self.M[k].append('-')
                    else:
                        self.M[k].append(dict())


        if len(self.M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in self.M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i>j and not(self.M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                if i<j:
                    dicio_aresta = self.M[i][j]
                    for k in dicio_aresta.values():
                        aresta = Aresta(k, dicio_aresta[k].getV1(), dicio_aresta[k].getV2())
                        if not(self.arestaValida(aresta)):
                            raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

    def arestaValida(self, aresta=Aresta()):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Verifica se os vértices existem no Grafo
        if type(aresta) == Aresta and self.existeVertice(aresta.getV1()) and self.existeVertice(aresta.getV2()):
            return True
        return False

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != ''

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return GrafoMatrizAdjacenciaNaoDirecionado.verticeValido(vertice) and vertice in self.N

    def __indice_do_vertice(self, v: str):
        '''
        Dado um vértice retorna o índice do vértice a na lista de vértices
        :param v: O vértice a ser analisado
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(v)

    def existeAresta(self, a: Aresta):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        if GrafoMatrizAdjacenciaNaoDirecionado.arestaValida(self, a):
            if a.getRotulo() in self.M[self.__indice_do_vertice(a.getV1())][self.__indice_do_vertice(a.getV2())]:
                return True
        return False

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if GrafoMatrizAdjacenciaNaoDirecionado.existeVertice(v):
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(dict()) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(dict())  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, rotulo='', v1='', v2='', peso=1):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''

        a = Aresta(rotulo, v1, v2, peso)

        if self.existeAresta(a):
            raise ArestaInvalidaException('A aresta {} já existe no Grafo'.format(a))

        if self.arestaValida(a):
            i_a1 = self.__indice_do_vertice(v1)
            i_a2 = self.__indice_do_vertice(v2)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2][rotulo] = a
            else:
                self.M[i_a2][i_a1][rotulo] = a
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

        return True

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        grafo_str = '  '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                if self.M[l][c] == '-':
                    grafo_str += str(self.M[l][c]) + ' '
                else:
                    if bool(self.M[l][c]):
                        grafo_str += '*' + ' '
                    else:
                        grafo_str += 'o' + ' '
            grafo_str += '\n'

        for l in range(len(self.N)):
            for c in range(len(self.N)):
                if bool(self.M[l][c]) and self.M[l][c] != '-':
                    grafo_str += self.N[l] + '-' + self.N[c] + ': '
                    for k in self.M[l][c]:
                        grafo_str += k + ' | '
                    grafo_str += '\n'

        return grafo_str



























