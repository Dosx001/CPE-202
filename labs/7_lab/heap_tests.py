import unittest
from heap import *

class TestHeap(unittest.TestCase):
        
    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        self.assertIsNone(test_heap.peek())
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.peek(),10)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])
        self.assertFalse(test_heap.enqueue(1))

    def test_02_dequeue(self):
       test_heap = MaxHeap()
       self.assertIsNone(test_heap.dequeue())
       test_heap.build_heap([2, 9, 7, 6, 5, 8])
       self.assertEqual(test_heap.dequeue(), 9)
       self.assertEqual(test_heap.get_size(), 5)
       self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(1)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_04_build_heap(self):
        test_heap = MaxHeap(8)
        built = test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(5)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        self.assertEqual(test_heap.heap_sort_ascending(list1), [2, 5, 6, 7, 8, 9])

    def test_letter(self):
        test_heap = MaxHeap()
        lista = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertEqual(test_heap.heap_sort_ascending(lista), ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_nega(self):
        test_heap = MaxHeap()
        lista = [-5,-1,-15,1,5,-7,7]
        for i in lista:
            test_heap.enqueue(i)
        test_heap.dequeue()
        test_heap.dequeue()
        test_heap.enqueue(25)
        test_heap.enqueue(-25)
        self.assertEqual(test_heap.contents(),[25, 1, -7, -5, -1, -15, -25])

    def test_nega2(self):
        test_heap = MaxHeap()
        lista = [-30, 36, 40, -79, 21, -75, -5]
        for i in lista:
            test_heap.enqueue(i)
        test_heap.dequeue()
        test_heap.dequeue()
        test_heap.enqueue(10)
        test_heap.enqueue(-94)
        self.assertEqual(test_heap.contents(),[21, 10, -5, -79, -30, -75, -94])

    def test_nega3(self):
        test_heap = MaxHeap()
        lista = [33, -61, -23, 42, 78, -10, -71, -69]
        for i in lista:
            test_heap.enqueue(i)
        test_heap.dequeue()
        test_heap.dequeue()
        test_heap.enqueue(-78)
        test_heap.enqueue(4)
        self.assertEqual(test_heap.contents(),[33, 4, -10, -61, -78, -23, -71, -69])

    def test_nega4(self):
        test_heap = MaxHeap()
        lista = [-50, -33]
        for i in lista:
            test_heap.enqueue(i)
        test_heap.dequeue()
        test_heap.dequeue()
        test_heap.enqueue(-78)
        test_heap.enqueue(4)
        self.assertEqual(test_heap.contents(),[4, -78])

  
if __name__ == "__main__":
    unittest.main()
