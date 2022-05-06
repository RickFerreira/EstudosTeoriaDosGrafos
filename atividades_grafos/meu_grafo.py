from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):
#
    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. O conjunto terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        #nos primeiros for ele coloca um indice pra comparar 
        vna = set()
        
        for v1 in self.N:
            for v2 in self.N:
                #verifica item por item comparado com outros itens e ve se existe ele na lista de arestas, assim irá saber se tem alguma aresta com aqueles indices
                achei = False
                for a in self.A:
                    if (v1 != v2):
                        if ((v1 == self.A[a].getV1() and v2 == self.A.[a].getV2()) or (v2 == self.A[a].getV1() and v1 == self.A.[a].getV2()):
                            (v2 == self.A[a].getV1() and V1 == self.A[a].getV2()):
                            achei = True
                if not achei and v1 != v2:           
                    vna.add("{}-{}").format((v1, v2)
                                            
        return vna
        
        
        '''vertices_nao_adjacentes = []

        for i in self.N:
            vertices_adjacentes = []
            for j in self.A:
                v1 = self.A[j].getV1()
                v2 = self.A[j].getV2()
                if v1 == i:
                    vertices_adjacentes.append(v2)
                elif v2 == i:
                    vertices_adjacentes.append(v1)

            for k in self.N:
                if k != i and k not in vertices_adjacentes:
                    a_test_1 = f'{k}-{k}'
                    a_test_2 = f'{k}-{i}'
                    if a_test_1 not in vertices_nao_adjacentes and a_test_2 not in vertices_nao_adjacentes:
                        vertices_nao_adjacentes.append(f'{i}-{k}')

            vertices_adjacentes = []

        return vertices_nao_adjacentes
        '''
    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertices_adjacentes = []

        verticeExiste = False

        for vt in self.N:
            if vt == V:
                verticeExiste = True
                vertices_adjacentes = []
                for a in self.A:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == vt:
                        vertices_adjacentes.append(v2)
                    if v2 == vt:
                        vertices_adjacentes.append(v1)

        if len(vertices_adjacentes) == 0 and verticeExiste == False:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo')
        else:
            return len(vertices_adjacentes)

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a1 in self.A:
            v1_a1 = self.A[a1].getV1()
            v2_a1 = self.A[a1].getV2()

            a1_str = f'{v1_a1}-{v2_a1}'
            a1_str_swap = f'{v2_a1}-{v1_a1}'

            for a2 in self.A:
                if a1 != a2:
                    v1_a2 = self.A[a2].getV1()
                    v2_a2 = self.A[a2].getV2()
                    a2_str = f'{v1_a2}-{v2_a2}'
                    a2_str_swap = f'{v2_a2}-{v1_a2}'

                    if a1_str == a2_str or a1_str == a2_str_swap or a2_str == a1_str_swap:
                        return True

        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas_adjacentes = []

        verticeExiste = False

        for vt in self.N:
            if vt == V:
                verticeExiste = True
                for a in self.A:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == vt or v2 == vt:
                        if a not in arestas_adjacentes:
                            arestas_adjacentes.append(a)

        if len(arestas_adjacentes) == 0 and verticeExiste == False:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo')
        else:
            return arestas_adjacentes

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False

        else:
            totalVertices = len(self.N)
            for v in self.N:
                if self.grau((v)) == totalVertices - 1:
                    continue
                else:
                    return False

            return True

    def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass
