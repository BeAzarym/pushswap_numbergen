import sys
import random

def generate_random_list(length, min, max):
	random_list = random.sample(range(min, max), length)
	return random_list

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Usage 	: python3 pushswap_gen.py <length> <min> <max>")
		print("Example	: python3 pushswap_gen.py 10 -10 10")
		sys.exit(1)
	length = int(sys.argv[1])
	min = int(sys.argv[2])
	max = int(sys.argv[3])
	random_list = generate_random_list(length, min, max)
	random_list_str = ' '.join(str(num) for num in random_list)
	print(random_list_str)