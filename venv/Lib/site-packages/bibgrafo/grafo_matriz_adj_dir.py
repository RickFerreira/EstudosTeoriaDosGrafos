from bibgrafo.grafo import GrafoIF
from bibgrafo.aresta import ArestaDirecionada
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class GrafoMatrizAdjacenciaDirecionado(GrafoIF):

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
            if not(GrafoMatrizAdjacenciaDirecionado.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')


        self.N = deepcopy(V)

        if M == []:
            self.M = list()
            for k in range(len(V)):
                self.M.append(list())
                for l in range(len(V)):
                    self.M[k].append(dict())

        if len(self.M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in self.M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        # Verifica se as arestas passadas na matriz são válidas
        for i in range(len(V)):
            for j in range(len(V)):
                dicio_aresta = self.M[i][j]
                for k in dicio_aresta.values():
                    aresta = ArestaDirecionada(k, dicio_aresta[k].getV1(), dicio_aresta[k].getV2())
                    if not(self.arestaValida(aresta)):
                        raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

    def arestaValida(self, aresta=ArestaDirecionada()):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Verifica se os vértices existem no Grafo
        if type(aresta) == ArestaDirecionada and self.existeVertice(aresta.getV1()) and self.existeVertice(aresta.getV2()):
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
        return GrafoMatrizAdjacenciaDirecionado.verticeValido(vertice) and vertice in self.N

    def __indice_do_vertice(self, v: str):
        '''
        Dado um vértice retorna o índice do vértice a na lista de vértices
        :param v: O vértice a ser analisado
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(v)

    def existeAresta(self, a: ArestaDirecionada):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        if GrafoMatrizAdjacenciaDirecionado.arestaValida(self, a):
            if a.getRotulo() in self.M[self.__indice_do_vertice(a.getV1())][self.__indice_do_vertice(a.getV2())]:
                return True
        return False

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if self.existeVertice(v):
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                self.M[k].append(dict())  # adiciona os elementos da coluna do vértice
                if k != len(self.N) -1:
                    self.M[self.N.index(v)].append(dict())  # adiciona um zero no último elemento da linha

        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, rotulo='', v1='', v2='', peso=1):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o vértice de origem e Y é o vértice de destino
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''

        a = ArestaDirecionada(rotulo, v1, v2, peso)

        if self.existeAresta(a):
            raise ArestaInvalidaException('A aresta {} já existe no Grafo'.format(a))

        if self.arestaValida(a):
            i_a1 = self.__indice_do_vertice(v1)
            i_a2 = self.__indice_do_vertice(v2)
            self.M[i_a1][i_a2][rotulo] = a
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

        return True

    def __eq__(self, other):
        '''
        Define a igualdade entre a instância do GrafoListaAdjacencia para o qual essa função foi chamada e a instância de um GrafoListaAdjacencia passado como parâmetro.
        :param other: O grafo que deve ser comparado com este grafo.
        :return: Um valor booleano caso os grafos sejam iguais.
        '''
        if len(self.M) != len(other.M) or len(self.N) != len(other.N):
            return False
        for n in self.N:
            if not other.existeVertice(n):
                return False
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[i][j]) != len(other.M[i][j]):
                    return False
                for k in self.M[i][j]:
                    if k not in other.M[i][j]:
                        return False
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
                if bool(self.M[l][c]):
                    grafo_str += '*' + ' '
                else:
                    grafo_str += 'o' + ' '
            grafo_str += '\n'

        for l in range(len(self.N)):
            for c in range(len(self.N)):
                if bool(self.M[l][c]):
                    grafo_str += self.N[l] + '-' + self.N[c] + ': '
                    for k in self.M[l][c]:
                        grafo_str += k
                    grafo_str += '\n'

        return grafo_str
