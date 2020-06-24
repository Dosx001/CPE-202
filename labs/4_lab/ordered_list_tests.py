import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(100)
        self.assertEqual(t_list.python_list(), [100])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(100), 0)
        self.assertTrue(t_list.search(100))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [100])
        self.assertTrue(t_list.remove(100))
        t_list.add(100)
        self.assertEqual(t_list.pop(0), 100)
        t_list.add(100)
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10,100])

    def test_not_simple(self):
        a=OrderedList()
        a.add(5)
        a.add(10)
        a.add(15)
        a.add(12)
        a.add(20)
        a.add(20)
        a.add(4)
        a.add(17)
        a.add(25)
        self.assertFalse(a.remove(16))
        self.assertFalse(a.index(16))
        with self.assertRaises(IndexError):
            a.pop(-1)
        with self.assertRaises(IndexError):
            a.pop(8)
        self.assertFalse(a.search(16))
        self.assertEqual(a.python_list_reversed(),[25, 20, 17, 15, 12, 10, 5, 4])
        self.assertEqual(a.size(),8)

    def test_empty_list(self):
        a=OrderedList()
        self.assertTrue(a.is_empty())
        self.assertFalse(a.remove(6))
        self.assertFalse(a.index(6))
        self.assertIsNone(a.index(6))
        print(a.index(6))
        with self.assertRaises(IndexError):
            a.pop(6)
        self.assertFalse(a.search(6))
        self.assertEqual(a.python_list(),[])
        self.assertEqual(a.python_list_reversed(),[])
        self.assertEqual(a.size(),0)

if __name__ == '__main__': 
    unittest.main()
