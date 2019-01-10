import random

def generate_digits(length):
	digits = []
	for i in range(length):
		digits.append(random.randrange(10))
	return digits

def write_digits(file_name, digits):
	with open(file_name, 'w') as f:
		for d in digits:
			f.write(str(d))

def get_max_repeats(digits):
	if len(digits) == 0:
		return []
	max_length = 0 
	digit = digits[0]
	length = 1
	for d in digits[1:]:
		if d == digit:
			length += 1
		else:
			if max_length < length:
				max_digit = digit
				max_length = length
			digit = d
			length = 1
	if max_length < length:
		max_digit = digit
		max_length = length		
	return [max_digit] * max_length

def print_repeats(repeats):
	for r in repeats:
		print(r)

if __name__ == '__main__':
	from sys import argv
	length = int(argv[1])
	file_name = argv[2]

	digits = generate_digits(length)
	write_digits(file_name, digits)
	repeats = get_max_repeats(digits)
	print_repeats(repeats)