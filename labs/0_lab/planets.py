def weight_on_planets():
	x = int(input('What do you weigh on earth? '))
	y = f'\nOn Mars you would weigh {x * .38} pounds.'
	z = f'\nOn Jupiter you would weigh {x * 2.34} pounds.'
	print(y + z)


if __name__ == '__main__':
	weight_on_planets()

