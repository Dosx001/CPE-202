import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
       g = Graph('test2.txt')
       g.add_vertex("v10")
       self.assertEqual(g.get_vertex("v10"), "v10")
       self.assertIsNone(g.get_vertex("v11"))
       g.add_edge("v1", "v10")
       self.assertEqual(g.get_vertices(), ['v1', 'v10', 'v2', 'v3', 'v4', 'v6', 'v7', 'v8']) 

    def test_04(self):
        g = Graph("test3.txt")
        self.assertEqual(g.conn_components(), [['D', 'E', 'F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N'], ['U', 'W', 'X', 'Y', 'Z']])
        self.assertFalse(g.is_bipartite())

    def test_05(self):
        g = Graph("test4.txt")
        self.assertEqual(g.conn_components(), [['A', 'B', 'C'], ['O', 'P', 'R', 'S', 'T']])
        self.assertFalse(g.is_bipartite())

    def test_06(self):
        g = Graph("num.txt")
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4', '5']])

if __name__ == '__main__':
   unittest.main()
