import unittest
from queue_array import Queue
#from queue_linked import Queue as Queue2

class TestLab_array(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        self.assertEqual(q.peek(),'thing')
        q.dequeue()
        with self.assertRaises(IndexError):
            q.peek()
        q.size()

    def test_empty_queue(self):
        q = Queue(0)
        with self.assertRaises(IndexError):
            q.enqueue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue2(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue(4)
        self.assertFalse(q.is_full())


class TestLab_link(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue2(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        self.assertEqual(q.peek(),'thing')
        q.dequeue()
        with self.assertRaises(IndexError):
            q.peek()
        q.size()

    def test_empty_queue(self):
        q = Queue2(0)
        with self.assertRaises(IndexError):
            q.enqueue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue2(self):
        q = Queue2(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue(4)
        self.assertFalse(q.is_full())


if __name__ == '__main__': 
    unittest.main()
