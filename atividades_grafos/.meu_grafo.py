from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()
        #percorrer a lista de vertices
        for i in self.N:
            for j in self.N:
                achei = False
                #percorre a lista de arestas
                for k in self.A:
                    if i != j:
                        #se naquela aresta o i e o j atual forem encontrados idependente da ordem,
                        #quer dizer que naquela configuração existe aresta, ou seja i e j são adjacente
                        if (i == self.A[k].getV1() and j == self.A[k].getV2()) or \
                                (j == self.A[k].getV1() and i == self.A[k].getV2()):
                            achei = True
                #cria uma dupla de arestas que não tem ligação
                if not achei and i != j:
                    vna.add("{}-{}".format(i, j))
        #retorna a lista criada com todos os itens não adjacentes
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        saida = False
        #percorre a lista de arestas
        for i in self.A:
            #verifica se o v1 é igual ao v2 naquela aresta
            if self.A[i].getV1() == self.A[i].getV2():
                #caso for troca a saida para verdadeiro
                saida = True
        return saida

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        achouOVertice = False
        numeroDeGraus = 0
        for i in self.N:
            #percorrendo toda a lista de vertices para procurar o V
            if i == V:
                #achou o V e agora vai olhar quantas arestas tem
                achouOVertice = True
                #percorre alista de arestas e verifica se o v1 ou o v2 de cada aresta é igual ao vertice achado
                for j in self.A:
                    if self.A[j].getV1() == i:
                        numeroDeGraus += 1
                    if self.A[j].getV2() == i:
                        numeroDeGraus += 1
                #a quantidade de vezes que aparece o vertice nas arestas é o grau dele
        #se não achar o vertice pedido da o erro
        if not achouOVertice:
            raise VerticeInvalidoException()
        else:
            return numeroDeGraus

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        saida = False
        #percorrendo a lista de arestas
        for i in self.A:
            cont = 0
            #procurando se existem arestas iguais ou as mesmas só trocando a ordem
            for j in self.A:
                if (self.A[i].getV1() == self.A[j].getV1()) and (self.A[i].getV2() == self.A[j].getV2()):
                    cont += 1
                elif (self.A[i].getV1() == self.A[j].getV2()) and (self.A[i].getV2() == self.A[j].getV1()):
                    cont += 1
            #verificando se achou iguais pelos menos duas vezes para poder ser paralela
            if cont >= 2:
                saida = True
        return saida

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        achouOVertice = False
        listaArestas = set()
        for i in self.N:
            #percorrendo toda a lista de vertices para procurar o V
            if i == V:
                achouOVertice = True
            #achou o V e agora vai percorrer a lista de arestas
                for j in self.A:
                    #se na aresta atual o v1 ou o v2 forem igual ao vertice passado adiciona então a aresta na lista
                    if (self.A[j].getV1() == V) or (self.A[j].getV2() == V):
                        listaArestas.add("{}".format(j))
        #se não achar o vertice pedido da o erro
        if not achouOVertice:
            raise VerticeInvalidoException()
        else:
            #retorna a lista de arestas
            return listaArestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        #nesse caso vou ter que chamar outras funções que já fiz para descobrir se é completo
        #grafo completo não tem laço, não te paralela e todos os vertices se conectam
        saida = True
        #verificando quantas vertices tem
        numeroDeVertices = len(self.N)
        #se tiver laço não é completo
        if self.ha_laco():
            saida = False
        #se tiver paralela não é completo
        elif self.ha_paralelas():
            saida = False
        #percorrendo a lista de vertices para verificar se todos são tocados
        for i in self.N:
            #verificando quantos graus tem cada vertice de acordo com a função grau
            grau = self.grau(i)
            #para cada vertice eu vejo se ele toca na mesma quantidade de vertices total menos ele mesmo
            if grau < numeroDeVertices-1:
                #ja sabendo que não tem laço e paralela verifico só se o grau tá correto
                #se o grau atual for menor do que o número de vertices-1 quer dizer que não seria completo pois faltaria tocar em algum
                saida = False
        #se tiver passado por todos sem mudar a saida ela vai ser true
        return saida

    def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass
