import random

specials = ['!','@','#','$','%','^','&','*']
caps = [chr(i) for i in range(65,91)]
lowers = [i.lower() for i in caps]

def main(len):
	xpass = ""
	for i in range(len):
		xpass += chr(random)