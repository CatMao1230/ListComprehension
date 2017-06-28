def generate_list_and_sum(start, end):
	ls = [x ** 2 if x % 2 == 1 else -(x ** 2) for x in range(start, end)]
	return sum(ls)

if __name__ == '__main__':
	print generate_list_and_sum(1, 11)