import unittest
from lab1 import *

class TestLab1(unittest.TestCase):
	def test_max_list_iter(self):
		"""Testing when input is None"""
		tlist=None
		with self.assertRaises(ValueError):
			max_list_iter(tlist)
		"""Testing when input is an empty list"""
		tlist=[]
		self.assertEqual(max_list_iter(tlist),None)
		"""Testing a list of ints"""
		tlist=[1,2,5,3,4]
		self.assertEqual(max_list_iter(tlist),5)

	def test_reverse_rec(self):
		"""Testing a list of ints"""
		self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
		"""Testing when the input is None"""
		with self.assertRaises(ValueError):
			reverse_rec(None)
		self.assertEqual(reverse_rec([]),[])

	def test_bin_search(self):
		"""Testing a list of ints"""
		list_val =[0,1,2,3,4,7,8,9,10]
		low = 0
		high = len(list_val)-1
		self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
		"""Testing if input is None"""
		with self.assertRaises(ValueError):
			bin_search(5,0,1,None)
		"""Testing when the return int is a high vaule"""
		self.assertEqual(bin_search(10,0,high,list_val),8)
		"""Testing when the return int is a low vaule"""
		self.assertEqual(bin_search(1,0,high,list_val),1)
		"""Testing when the target vaule is not in the list of ints"""
		self.assertEqual(bin_search(11,0,high,list_val),None)
		self.assertIsNone(bin_search(2,0,high,[]))

if __name__=="__main__":
	unittest.main()
