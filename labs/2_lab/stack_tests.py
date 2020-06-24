import unittest

from stack_array import Stack
from stack_linked import Stack as Stack2

class TestLab2_array(unittest.TestCase):
	def test_simple(self):
		stack = Stack(5)
		stack.push(0)
		self.assertFalse(stack.is_empty())
		self.assertFalse(stack.is_full())
		self.assertEqual(stack.size(),1)

	def test_empty_stack(self):
		stack = Stack(0)
		with self.assertRaises(IndexError):
			stack.pop()
		with self.assertRaises(IndexError):
			stack.peek()
		with self.assertRaises(IndexError):
			stack.push(1)

	def test_stack(self):
		stack = Stack(2)
		stack.push(1)
		stack.push(2)
		self.assertEqual(stack.pop(),2)
		self.assertEqual(stack.peek(),1)

class TestLab2_link(unittest.TestCase):
	def test_simple(self):
		stack = Stack2(5)
		stack.push(0)
		self.assertFalse(stack.is_empty())
		self.assertFalse(stack.is_full())
		self.assertEqual(stack.size(),1)

	def test_empty_stack(self):
		stack = Stack2(0)
		with self.assertRaises(IndexError):
			stack.pop()
		with self.assertRaises(IndexError):
			stack.peek()
		with self.assertRaises(IndexError):
			stack.push(1)

	def test_stack(self):
		stack = Stack2(2)
		stack.push(1)
		stack.push(2)
		self.assertEqual(stack.pop(),2)
		self.assertEqual(stack.peek(),1)



if __name__ == '__main__': 
    unittest.main()
