import unittest
from perm_lex import *

class TestAssign1(unittest.TestCase):

	def test_perm_gen_lex_0(self):
		self.assertEqual(perm_gen_lex(''),[])

	def test_perm_gen_lex_1(self):
		self.assertEqual(perm_gen_lex('a'),['a'])

	def test_perm_gen_lex_2(self):
		self.assertEqual(perm_gen_lex('ab'),['ab','ba'])

	def test_perm_gen_lex_3(self):
		self.assertEqual(perm_gen_lex('abc'),['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])


if __name__ == "__main__":
	unittest.main()
