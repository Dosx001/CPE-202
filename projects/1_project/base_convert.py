def convert(num, b):
	"""Recursive function that returns a string representing num in the base b"""
	rem = num % b
	num = num // b
	if num == 0:
		return f'{rem}' if rem < 10 else chr(55 + rem)
	return convert(num, b) + f'{rem}' if rem < 10 else convert(num, b) + chr(55 + rem)

