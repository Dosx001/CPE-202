import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
	def test_postfix_eval_01(self):
		self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

	def test_postfix_eval_02(self):
		try:
			postfix_eval("blah")
		except PostfixFormatException as e:
			self.assertEqual(str(e), "Invalid token")

	def test_postfix_eval_03(self):
		try:
			postfix_eval("4 +")
		except PostfixFormatException as e:
			self.assertEqual(str(e), "Insufficient operands")

	def test_postfix_eval_04(self):
		try:
			postfix_eval("1.0 2 3 +")
		except PostfixFormatException as e:
			self.assertEqual(str(e), "Too many operands")

	def test_postfix_eval_05(self):
		with self.assertRaises(ValueError):
			postfix_eval("1 0 /")

	def test_postfix_eval_06(self):
		try:
			postfix_eval("3 5 / 2 >>")
		except PostfixFormatException as e:
			self.assertEqual(str(e),"Illegal bit shift operand")

	def test_infix_to_postfix_01(self):
		self.assertEqual(infix_to_postfix("6.0 - 3"), "6.0 3 -")
		self.assertEqual(infix_to_postfix("6"), "6")

	def test_infix_to_postfix_02(self):
		input1="8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1 ) - 3 )"
		output="8 3 4 * + 6 2 - 2 6 3 / 1 - * + 3 - +" 
		self.assertEqual(infix_to_postfix(input1),output)

	def test_infix_to_postfix_03(self):
		input="3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"
		output="3 4 2 * 1 5 - 2 3 ** ** / +"
		self.assertEqual(infix_to_postfix(input),output)

	def test_infix_to_postfix_04(self):
		input="4 + ( 2 / 3 - 4 ) + ( 6 - 5 ) * 8"
		output="4 2 3 / 4 - + 6 5 - 8 * +"
		self.assertEqual(infix_to_postfix(input),output)

	def test_prefix_to_postfix_01(self):
		self.assertEqual(prefix_to_postfix("* - 3.0 / 2 1 - / 4 5 6"), "3.0 2 1 / - 4 5 / 6 - *")

	def test_infix_to_postfix_complex(self):
		self.assertEqual("2 38 1.2 3.6 ** * 2.8 6 ** / 3.7 2 << 5 3 ** / + 23 + 1.1 >> 2.2 ** 2.4 5 / - 1 - + 1.6 3 9 << 2.8 ** ** 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 ** 5.2 9.9 ** / / - + - +", infix_to_postfix("2 + ( ( ( ( 38 * 1.2 ** 3.6 / 2.8 ** 6 ) + 3.7 << 2 / 5 ** 3 + 23 ) >> 1.1 ** 2.2 ) - 2.4 / 5 - 1 ) + ( 1.6 ** 3 << 9 ** 2.8 - 3 - ( 6.2 / 4 + ( 12.8 * 2 / 1.1 - 4.4 / ( 3.2 ** 1.1 / 5.2 ** 9.9 ) ) ) )"))	
	def test_prefix_to_postfix_complex(self):
		 self.assertEqual(prefix_to_postfix("+ + 2 - - + + * 38 1.2 / / * 3.6 ** 1.8 ** .25 1.7 2 ** 5 3 / 23 ** 1.1 2.2 / 2.4 5 1 - * * 1.6 ** 3 9 2.8 ** 3 / 6.2 ** 4 - - * 12.8 ** 2 1.1 / 4.4 3.2 / 1.1 ** 5.2 7.7"), "2 38 1.2 * 3.6 1.8 .25 1.7 ** ** * 2 / 5 3 ** / + 23 1.1 2.2 ** / + 2.4 5 / - 1 - + 1.6 3 9 ** * 2.8 * 3 6.2 4 12.8 2 1.1 ** * 4.4 3.2 / - 1.1 5.2 7.7 ** / - ** / ** - +")

if __name__ == "__main__":
    unittest.main()
