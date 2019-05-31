import itertools


chars = input ("chars: ")
min_len = int(input("min: "))
max_len = int(input("max: "))
filename = input ("filename: ")


def create_pass_file(chars, min_len, max_len, filename):
	opf = open (filename, "w")
	for leng in range(min_len, max_len+1):
		passwords = itertools.product(chars, repeat=leng)
		for password in passwords:
			password = ''.join(password)
			opf.write(password + "\n")

	print (filename + " Generated")
	opf.close()


def count_lines(filename):
	f = open (filename, "r")
	num_lines = sum(1 for line in f)
	print ("Password List Contains: " + str(num_lines) + " Passwords")

def main():
	create_pass_file(chars, min_len, max_len, filename)
	count_lines(filename)

	

main()