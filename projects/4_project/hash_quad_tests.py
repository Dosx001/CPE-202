import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def setUp(self):
        self.ht = HashTable(7)
    
    def test_01a(self):
        self.assertEqual(self.ht.get_table_size(), 7)

    def test_01b(self):
        self.assertEqual(self.ht.get_num_items(), 0)

    def test_01c(self):
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_01d(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])

    def test_01e(self):
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01f(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01g(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)

    def test_01h(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)

    def test_02a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_02b(self):
        ht = HashTable(15)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)
        ht.insert("tac", 5)
        self.assertEqual(ht.get_num_items(), 2)
        ht.insert("tac", 5)
        self.assertEqual(ht.get_num_items(), 2)

    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        ht = HashTable(15)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)
        ht.insert("tac",5)
        self.assertEqual(ht.in_table("tac"), True)
        self.assertEqual(ht.in_table("act"), False)

    def test_02f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self):
        ht = HashTable(15)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 12)
        ht.insert("tac",5)
        self.assertEqual(ht.get_index("tac"),13)
        self.assertIsNone(ht.get_index("act"))

    def test_03(self):
        ht = HashTable(15)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        self.assertEqual(ht.get_value("cat"), [5, 17])
        ht.insert("tac", 5)
        ht.insert("tac", 10)
        self.assertEqual(ht.get_value("tac"), [5, 10])
        self.assertIsNone(ht.get_value("act"))

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", 8)
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", 10)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", 12) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

#    def test_05(self):
#        ht = HashTable(199)
#        for i in range(100):
#            ht.insert(f'mousehouse{i}', i)
#            #print(ht.get_table_size())
#            print("")

if __name__ == '__main__':
   unittest.main()
