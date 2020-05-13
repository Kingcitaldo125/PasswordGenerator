import random
import sys


specials = ['!','@','#','$','%','^','&','*']
caps = [chr(i) for i in range(65,91)]
lowers = [i.lower() for i in caps]


def main(mlen):
	global specials
	global caps
	global lowers
	
	xpass = ""
	for i in range(mlen):
		rc = int(random.randrange(0,3))
		if rc == 0:
			xpass += specials[random.randrange(0, len(specials))]
		elif rc == 1:
			xpass += caps[random.randrange(0, len(caps))]
		else:
			xpass += lowers[random.randrange(0, len(lowers))]
	
	return xpass


if __name__ == "__main__":
	passwd = main(int(sys.argv[1]))
	print("Passwd:", passwd)
