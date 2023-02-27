import sys
import random

def generate_random_list(length):
	random_list = random.sample(range(-length**2, length**2), length)
	return random_list

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage : python3 pushswap_gen.py <length>")
		sys.exit(1)
	length = int(sys.argv[1])
	random_list = generate_random_list(length)
	print("Just generate", length,"random number\n",random_list)