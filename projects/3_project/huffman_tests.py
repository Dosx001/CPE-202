import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertEqual(parse_header("97 2 98 4 99 8 100 16 102 2")[97:104],anslist)

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode(self):
        huffman_decode("declaration_out.txt", "declaration_decoded.txt")
        err = subprocess.call("diff -wb declaration_decoded.txt declaration.txt", shell = True)
        self.assertEqual(err, 0)

    def test_big_boi(self):
        huffman_encode("War_And_Peace.txt","War_And_Peace_out.txt")
        huffman_decode("War_And_Peace_out.txt","War_And_Peace_decoded.txt")
        err = subprocess.call("diff -wb War_And_Peace_decoded.txt War_And_Peace.txt", shell = True)
        self.assertEqual(err,0)

    def test_letter(self):
        huffman_encode("letter.txt", "letter_out.txt")
        huffman_decode("letter_out.txt","letter_decoded.txt")
        err = subprocess.call("diff -wb letter_decoded.txt letter.txt", shell = True)
        self.assertEqual(err, 0)

    def test_blank(self):
        huffman_encode("blank.txt", "blank_out.txt")
        huffman_decode("blank_out.txt","blank_decoded.txt")
        err = subprocess.call("diff -wb blank_decoded.txt blank.txt", shell = True)
        self.assertEqual(err, 0)
    
    def test_line(self):
        huffman_encode("line.txt", "line_out.txt")
        huffman_decode("line_out.txt","line_decoded.txt")
        err = subprocess.call("diff -wb line_decoded.txt line.txt", shell = True)
        self.assertEqual(err, 0)
    
    def test_chr(self):
        huffman_encode("aaa.txt", "aaa_out.txt")
        huffman_decode("aaa_out.txt","aaa_decoded.txt")
        err = subprocess.call("diff -wb aaa_decoded.txt aaa.txt", shell = True)
        self.assertEqual(err, 0)
   
if __name__ == '__main__': 
   unittest.main()
