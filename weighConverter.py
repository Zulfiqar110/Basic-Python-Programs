print()
Weight = int(input("Enter Your Weight: "))  #converting string to integer as input takes str value
unit = input('(L)bs or (K)g: ')


if unit.upper() == 'L':
	Weight = Weight * 0.45 
	print(f'Your weight is {Weight} Kilograms.')

elif unit.upper() == 'K':
	Weight = Weight // 0.45     # // returns integer value whereas / returns float value
	print(f'Your Weight is {Weight} Pounds.')  # to use formatted strings just prefix the string with f.
else:
	print('Invalid Expression')

	

