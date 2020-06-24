import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_insert(self):
        nums=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
        n=len(nums)
        comps=insertion_sort(nums)
        #self.assertEqual(comps,n*(n-1)/2)
        self.assertEqual(nums,[2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])

    def test_select(self):
        nums=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
        n=len(nums)
        comps=selection_sort(nums)
        self.assertEqual(comps,n*(n-1)/2)
        self.assertEqual(nums,[2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])

    def test_count(self):
        nums=[0,5,2,1,7,3]
        comps=selection_sort(nums)
        self.assertEqual(15,comps)
        nums=[0,5,2,1,7,3]
        comps=insertion_sort(nums)
        self.assertEqual(10,comps)

  #  def test_main(self):
   #     self.assertIsNone(main())

   # def test_file(self):
    #    exec(open("sorts.py").read())

if __name__ == '__main__': 
    unittest.main()
