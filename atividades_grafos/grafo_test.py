import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'C')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p3.adicionaAresta('a', 'J', 'C')
        self.g_p3.adicionaAresta('a2', 'C', 'E')
        self.g_p3.adicionaAresta('a3', 'C', 'E')
        self.g_p3.adicionaAresta('a4', 'P', 'C')
        self.g_p3.adicionaAresta('a5', 'P', 'C')
        self.g_p3.adicionaAresta('a6', 'T', 'C')
        self.g_p3.adicionaAresta('a7', 'M', 'C')
        self.g_p3.adicionaAresta('a8', 'M', 'T')
        self.g_p3.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C')
        self.g_p4.adicionaAresta('a2', 'J', 'E')
        self.g_p4.adicionaAresta('a3', 'C', 'E')
        self.g_p4.adicionaAresta('a4', 'P', 'C')
        self.g_p4.adicionaAresta('a5', 'P', 'C')
        self.g_p4.adicionaAresta('a6', 'T', 'C')
        self.g_p4.adicionaAresta('a7', 'M', 'C')
        self.g_p4.adicionaAresta('a8', 'M', 'T')
        self.g_p4.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D'])

        #Grafo do roteiro 2 para testes by Rick
        self.g_t = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_t.adicionaAresta('1', 'A', 'B')
        self.g_t.adicionaAresta('2', 'A', 'G')
        self.g_t.adicionaAresta('3', 'A', 'J')
        self.g_t.adicionaAresta('4', 'G', 'K')
        self.g_t.adicionaAresta('5', 'K', 'J')
        self.g_t.adicionaAresta('6', 'J', 'G')
        self.g_t.adicionaAresta('7', 'J', 'I')
        self.g_t.adicionaAresta('8', 'I', 'G')
        self.g_t.adicionaAresta('9', 'G', 'H')
        self.g_t.adicionaAresta('10', 'H', 'F')
        self.g_t.adicionaAresta('11', 'F', 'B')
        self.g_t.adicionaAresta('12', 'B', 'G')
        self.g_t.adicionaAresta('13', 'B', 'C')
        self.g_t.adicionaAresta('14', 'C', 'D')
        self.g_t.adicionaAresta('15', 'D', 'E')
        self.g_t.adicionaAresta('16', 'D', 'B')
        self.g_t.adicionaAresta('17', 'E', 'B')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z', 'E-J', 'P-J', 'M-J', 'T-J', 'Z-J', 'Z-C', 'P-E', 'M-E', 'T-E', 'Z-E', 'M-P', 'T-P',
                          'Z-P',
                          'Z-M'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'B-A', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    # testes de by Rick DFS
    def test_dfs(self):
        #teste no grafo da paraiba com todas as cidades
        self.assertEqual(set(self.g_p.dfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('C').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('E').A.keys()), set(['a2', 'a1', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('P').A.keys()), set(['a4', 'a1', 'a2', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('M').A.keys()), set(['a7', 'a1', 'a2', 'a4', 'a6', 'a9']))
        self.assertEqual(set(self.g_p.dfs('T').A.keys()), set(['a6', 'a1', 'a2', 'a4', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.dfs('Z').A.keys()), set(['a9', 'a6', 'a1', 'a2', 'a4', 'a7']))
        #teste no grafo sem paralelas
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('C').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('E').A.keys()), set(['a2', 'a1', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('P').A.keys()), set(['a3', 'a1', 'a2', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('M').A.keys()), set(['a5', 'a1', 'a2', 'a3', 'a4', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('T').A.keys()), set(['a4', 'a1', 'a2', 'a3', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('Z').A.keys()), set(['a7', 'a4', 'a1', 'a2', 'a3', 'a5']))
        #teste no primeiro grafo completo
        self.assertEqual(set(self.g_c.dfs('J').A.keys()), set(['a1', 'a4', 'a6']))
        self.assertEqual(set(self.g_c.dfs('C').A.keys()), set(['a1', 'a2', 'a6']))
        self.assertEqual(set(self.g_c.dfs('E').A.keys()), set(['a2', 'a1', 'a5']))
        self.assertEqual(set(self.g_c.dfs('P').A.keys()), set(['a3', 'a1', 'a4']))
        #Teste no segundo grafo completo
        self.assertEqual(set(self.g_c2.dfs('Nina').A.keys()), set(['amiga']))
        self.assertEqual(set(self.g_c2.dfs('Maria').A.keys()), set(['amiga']))
        #Teste grafo de exemplo do roteiro
        self.assertEqual(set(self.g_t.dfs('A').A.keys()), set(['1', '11', '10', '9', '4', '5', '7', '13', '14', '15']))
        self.assertEqual(set(self.g_t.dfs('B').A.keys()), set(['1', '2', '4', '5', '7', '9', '10', '13', '14', '15']))
        self.assertEqual(set(self.g_t.dfs('C').A.keys()), set(['13', '1', '2', '4', '5', '7', '9', '10', '16', '15']))

    # testes de by Rick BFS
    def test_bfs(self):
        #Teste de largura em todas as cidades grafos da paraiba
        self.assertEqual(set(self.g_p.bfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('C').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('E').A.keys()), set(['a2', 'a1', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('P').A.keys()), set(['a4', 'a1', 'a2', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('M').A.keys()), set(['a7', 'a8', 'a1', 'a2', 'a4', 'a9']))
        self.assertEqual(set(self.g_p.bfs('T').A.keys()), set(['a6', 'a8', 'a9', 'a1', 'a2', 'a4']))
        self.assertEqual(set(self.g_p.bfs('Z').A.keys()), set(['a9', 'a6', 'a8', 'a1', 'a2', 'a4']))
        #Teste grafo sem paralela
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('C').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('E').A.keys()), set(['a2', 'a1', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('P').A.keys()), set(['a3', 'a1', 'a2', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('M').A.keys()), set(['a5', 'a6', 'a1', 'a2', 'a3', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('T').A.keys()), set(['a4', 'a6', 'a7', 'a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('Z').A.keys()), set(['a7', 'a4', 'a6', 'a1', 'a2', 'a3']))
        #Teste no primeiro grafo completo
        self.assertEqual(set(self.g_c.bfs('J').A.keys()), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_c.bfs('C').A.keys()), set(['a1', 'a4', 'a5']))
        self.assertEqual(set(self.g_c.bfs('E').A.keys()), set(['a2', 'a4', 'a6']))
        self.assertEqual(set(self.g_c.bfs('P').A.keys()), set(['a3', 'a5', 'a6']))
        #Teste no segundo grafo completo
        self.assertEqual(set(self.g_c2.bfs('Nina').A.keys()), set(['amiga']))
        self.assertEqual(set(self.g_c2.bfs('Maria').A.keys()), set(['amiga']))
        #Teste grafo de exemplo do roteiro
        self.assertEqual(set(self.g_t.bfs('D').A.keys()), set(['14', '15', '16', '1', '11', '12', '3', '8', '4', '10']))
        self.assertEqual(set(self.g_t.bfs('G').A.keys()), set(['9', '16', '2', '13', '12', '8', '4', '10', '17', '6']))
        self.assertEqual(set(self.g_t.bfs('H').A.keys()), set(['13', '9', '2', '6', '12', '16', '10', '8', '17', '4']))
