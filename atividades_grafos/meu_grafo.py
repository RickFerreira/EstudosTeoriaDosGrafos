from collections import deque

from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
#Richard Ferreira Salviano
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
    
    #códigos de Rick grafos de profundidade e largura
    def vertices_Adjacentes(self):
        '''
        Richard Ferreira Salviano
        Criando uma função para gerar uma lista de vertices adjacentes
        '''
        #criando a lista
        verticesAdjacentes = {}
        #percorrendo as arestas
        for aresta in self.A:
            #armazenando a aresta atual
            arestaAtual = self.A[aresta]
            #Fazendo condições para verificar se o vertice tem adijacencia e adiconar na lista
            if arestaAtual.getV1() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV1()] = [(arestaAtual.getV2(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV1()].append((arestaAtual.getV2(), aresta))

            if arestaAtual.getV2() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV2()] = [(arestaAtual.getV1(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV2()].append((arestaAtual.getV1(), aresta))
        #retornando a lista com todos os vertices que tem adjacencia
        return verticesAdjacentes

    def dfs_recursivo(self, V, grafo_dfs, verticesPassados, verticesAdjacentes):
        '''
        Richard Ferreira Salviano
        Função para percorrer o grafo recursivamente
        '''

        verticesPassados.add(V)

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
        #Se o vertice não está na lista de vertices já passados
        #Eu vou e adiciono o vertice e aresta na lista
            if verticeAdjacente not in verticesPassados:
                grafo_dfs.adicionaAresta(rotuloAresta, V, verticeAdjacente)
                self.dfs_recursivo(verticeAdjacente, grafo_dfs, verticesPassados, verticesAdjacentes)

    def dfs(self, V=''):
        '''
        Richard Ferreira Salviano
        Receber como parâmetro qual o vértice será usado como raiz da árvore, para uma busca em profundidade
        Retornar a árvore DFS, representada por meio de um outro grafo que contém apenas as arestas que fazem parte da árvore
        '''
        #chamando a função para fazer uma lista adjacente
        verticesAdjacentes = self.vertices_Adjacentes()
        #recebendo o grafo
        grafo_dfs = MeuGrafo(self.N[::])
        #criando lista para ver os vertices que já foram visitados
        verticesPassados = set()
        #Se o vertice atual não for adjacente retorna o grafo atual
        if V not in verticesAdjacentes: return grafo_dfs
        #chamando a função recursiva
        self.dfs_recursivo(V, grafo_dfs, verticesPassados, verticesAdjacentes)
        #depois que rodar tudo retorna o grafo
        return grafo_dfs

    def bfs(self, V=''):
        '''
        Richard Ferreira Salviano
        Receber como parâmetro qual o vértice será usado como raiz da árvore, para uma busca em profundidade
        Retornar a árvore BFS, representada por meio de um outro grafo que contém apenas as arestas que fazem parte da árvore
        '''
        #gerando o grafo
        grafo_bfs = MeuGrafo(self.N[::])
        #criando lista para armazenar os vertices visitados
        verticesPassados = set([V])
        #chamando o deque para facilitar o trabalho com fila
        fila = deque([V])
        #gerando lista de vertices adjacentes
        verticesAdjacentes = self.vertices_Adjacentes()
        #Se o vertice atual não for adjacente retorna o grafo atual
        if V not in verticesAdjacentes: return grafo_bfs
        #percorrendo a fila até zerar
        while len(fila) != 0:
            #remove um elemento do lado esquerdo do deque e retorna o valor.
            verticeAtual = fila.popleft()

            for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[verticeAtual]:
                #Se o vertice ainda não foi acessado adciona ele no grafo
                if verticeAdjacente not in verticesPassados:
                    grafo_bfs.adicionaAresta(rotuloAresta, verticeAtual, verticeAdjacente)
                    verticesPassados.add(verticeAdjacente)
                    fila.append(verticeAdjacente)
        #depois de passar por todos os vertices retorna o grafo de busca em largura
        return grafo_bfs

    #Essa função só será feita depois
    def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass