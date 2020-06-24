import unittest
from concordance import *
#from concordance_node import *
import filecmp

class TestList(unittest.TestCase):

    def setUp(self):
        self.conc = Concordance()

    def test_01(self):
        self.conc.load_stop_table("stop_words.txt")
        self.conc.load_concordance_table("file1.txt")
        self.conc.write_concordance("file1_con.txt")
        self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))
    
    def test_02(self):
        self.conc.load_stop_table("stop_words.txt")
        self.conc.load_concordance_table("file2.txt")
        self.conc.write_concordance("file2_con.txt")
        self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))
    
    def test_03(self):
        self.conc.load_stop_table("stop_words.txt")
        self.conc.load_concordance_table("declaration.txt")
        self.conc.write_concordance("declaration_con.txt")
        self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    def test_04(self): #.29s
        self.conc.load_stop_table("stop_words.txt")
        self.conc.load_concordance_table("War_And_Peace.txt")
        self.conc.write_concordance("War_And_Peace_con.txt")
        self.assertTrue(filecmp.cmp("War_And_Peace_sol.txt", "War_And_Peace_con.txt"))

    def test_05(self):
        self.conc.load_stop_table("Dict_A-C.txt") #~2.6s
        fp = open("Dict_A-C.txt",'r')
        for line in fp.readlines(): #~1s
            line.split()
            self.conc.stop_table.in_table(line[0])
            self.conc.stop_table.get_value(line[0])
            self.conc.stop_table.get_index(line[0])
        fp.close()

    def test_06(self): #~1s
        self.conc.load_stop_table("stop_words_the.txt")
        self.conc.load_concordance_table("file_the.txt")
        self.conc.write_concordance("file_the_con.txt")

if __name__ == '__main__':
   unittest.main()
