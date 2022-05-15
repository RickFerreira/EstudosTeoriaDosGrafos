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
     
    
    #códigos de Rick grafos de profundidade e lateral
    def dfs(self, V=''):
        '''
        Richard Ferreira Salviano
        Receber como parâmetro qual o vértice será usado como raiz da árvore, para uma busca em profundidade
        Retornar a árvore DFS, representada por meio de um outro grafo que contém apenas as arestas que fazem parte da árvore
        '''

        finalizada = False

        vertices_examinados = {}

        for vt in self.N:
            vertices_examinados[vt] = {
                'examinado': False,
                'pai': '',
                'arestas': [],
                'ehPai': False
            }

        vertices_examinados[V] = {
            'examinado': True,
            'pai': V,
            'arestas': [],
            'ehPai': True
        }

        arestas_examinadas = []
        arestas_de_retorno = []

        vertice_atual = V

        comeco = True

        grafo_final = MeuGrafo()

        grafo_final.adicionaVertice(vertice_atual)

        while (finalizada != True):
            if vertices_examinados[vertice_atual]['examinado'] == True and vertice_atual != V:
                vertice_atual == vertices_examinados[V]['pai']
                continue

            elif comeco == False and vertice_atual == V:
                finalizada = True

            else:
                comeco = False
                vertices_examinados[vertice_atual]['arestas'] = self.arestas_sobre_vertice(vertice_atual)
                todas_arestas_examinadas = False

                qtd_arestas_incidentes = len(vertices_examinados[vertice_atual]['arestas'])
                cont = 0
                for aresta_incidente in vertices_examinados[vertice_atual]['arestas']:
                    cont += 1
                    if aresta_incidente not in arestas_examinadas:
                        todas_arestas_examinadas = False
                        v1 = self.A[aresta_incidente].getV1()
                        v2 = self.A[aresta_incidente].getV2()
                        if v1 == v2:
                            continue

                        if v1 == vertice_atual:
                            if vertices_examinados[v2]['examinado'] == False and vertices_examinados[v1][
                                'pai'] != v2 and vertices_examinados[v2]['ehPai'] == False:
                                vertices_examinados[v2]['pai'] = vertice_atual
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v2
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                        elif v2 == vertice_atual:
                            if vertices_examinados[v1]['examinado'] == False and vertices_examinados[v2][
                                'pai'] != v1 and vertices_examinados[v1]['ehPai'] == False:
                                vertices_examinados[v1]['pai'] = vertice_atual
                                vertices_examinados[vertice_atual]['ehPai'] = True
                                vertice_atual = v1
                                arestas_examinadas.append(aresta_incidente)

                                if v1 not in grafo_final.N: grafo_final.adicionaVertice(v1)
                                if v2 not in grafo_final.N: grafo_final.adicionaVertice(v2)

                                grafo_final.adicionaAresta(aresta_incidente, v1, v2)
                                break
                            else:
                                arestas_de_retorno.append(aresta_incidente)
                                if cont == qtd_arestas_incidentes:
                                    todas_arestas_examinadas = True
                                continue

                    todas_arestas_examinadas = True

                if todas_arestas_examinadas:
                    vertices_examinados[vertice_atual]['examinado'] = True
                    vertice_atual = vertices_examinados[vertice_atual]['pai']
                    continue

                else:
                    continue

        return grafo_final

    def bfs(self, V=''):
        '''
        Richard Ferreira Salviano
        Receber como parâmetro qual o vértice será usado como raiz da árvore, para uma busca em profundidade
        Retornar a árvore BFS, representada por meio de um outro grafo que contém apenas as arestas que fazem parte da árvore
        '''
        finalizada = False

        vertices_examinados = {}

        for vt in self.N:
            vertices_examinados[vt] = {
                'examinado': False,
                'root': False,
                'pai': False,
                'temPai': False,
                'arestaPai': ''
            }

        vertices_examinados[V] = {
            'examinado': True,
            'root': True,
            'pai': V,
            'temPai': True,
            'arestaPai': ''
        }

        vertice_atual = V

        comeco = True

        grafo_final = MeuGrafo()

        fila_vertices = []

        while (finalizada == False):
            arestas_incidentes = self.arestas_sobre_vertice(vertice_atual)
            for a in arestas_incidentes:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == v2:
                    continue

                if v1 == vertice_atual:
                    if not vertices_examinados[v2]['temPai']:
                        vertices_examinados[v2]['pai'] = v1
                        vertices_examinados[v2]['temPai'] = True
                        vertices_examinados[v2]['arestaPai'] = a

                    if vertices_examinados[v2]['examinado'] == False and v2 not in fila_vertices:
                        fila_vertices.append(v2)

                if v2 == vertice_atual:
                    if not vertices_examinados[v1]['temPai']:
                        vertices_examinados[v1]['pai'] = v2
                        vertices_examinados[v1]['temPai'] = True
                        vertices_examinados[v1]['arestaPai'] = a

                    if vertices_examinados[v1]['examinado'] == False and v1 not in fila_vertices:
                        fila_vertices.append(v1)

            vertices_examinados[vertice_atual]['examinado'] = True

            if vertices_examinados[vertice_atual]['examinado']:
                grafo_final.adicionaVertice(vertice_atual)

            if vertices_examinados[vertice_atual]['root'] == False:
                v_pai = vertices_examinados[vertice_atual]['pai']
                aresta_do_pai = vertices_examinados[vertice_atual]['arestaPai']

                grafo_final.adicionaAresta(aresta_do_pai, vertice_atual, v_pai)

            if vertice_atual in fila_vertices:
                fila_vertices.remove(vertice_atual)
                if len(fila_vertices) == 0:
                    finalizada = True
                    break

            vertice_atual = fila_vertices[0]

        return grafo_final
