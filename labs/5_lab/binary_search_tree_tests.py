import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertTrue(bst.delete(10))
        self.assertEqual(bst.tree_height(), None)

    def test_empty(self):
        bst=BinarySearchTree()
        self.assertEqual(bst.find_min(),None)
        self.assertEqual(bst.find_max(),None) 
        self.assertFalse(bst.delete(21))
        self.assertEqual(bst.inorder_list(),[])
        self.assertEqual(bst.preorder_list(),[])

    def test_tree(self):
        bst=BinarySearchTree()
        nums=[20,16,6,0,7,17,25,21,29,28,51,46,18]
        for i in nums:
            bst.insert(i)
        self.assertEqual(bst.inorder_list(),[0, 6, 7, 16, 17, 18, 20, 21, 25, 28, 29, 46, 51])
        self.assertEqual(bst.preorder_list(),[20, 16, 6, 0, 7, 17, 18, 25, 21, 29, 28, 51, 46])
        self.assertEqual(bst.find_min(),(0,None))
        self.assertEqual(bst.find_max(),(51,None)) 
        self.assertFalse(bst.search(45))
        self.assertEqual(bst.tree_height(),4)
        for i in nums:
            self.assertTrue(bst.delete(i))
        self.assertTrue(bst.is_empty())
    
    def test_tree2(self):
        bst=BinarySearchTree()
        nums=[3, 35, 71, 73, 41, 12, 48, 80, 49, 88]
        for i in nums:
            bst.insert(i)
        rm=[41, 3, 12, 71, 80, 73, 35, 88, 48, 49]
        for i in rm:
            bst.delete(i)
        self.assertTrue(bst.is_empty())
        nums=[32, 1, 97, 5, 14, 80, 81, 82, 51, 52, 21, 87, 95]
        for i in nums:
            bst.insert(i)
        rm=[21, 32, 95, 52, 97, 87, 51, 81, 82, 80, 1, 5, 14]
        for i in rm:
            bst.delete(i)
        self.assertTrue(bst.is_empty())
        nums=[96, 65, 64, 15, 20, 21, 24, 90]
        for i in nums:
            bst.insert(i)
        rm=[24, 65, 15, 90, 21, 96, 64, 20]
        for i in rm:
            bst.delete(i)
        self.assertTrue(bst.is_empty())

if __name__ == '__main__': 
    unittest.main()
