#!/usr/bin/python

# Sierpinski Carpet (v1)
	

import sys


def pattern_ver_xxx_xdd(gc, lc, hc): # vertical xxx / xdd to print horizontal xxx / xdd
	
	if lc%2 == 0 and hc%2 == 0:
		print(" ", end='')
	else:
		print("#", end='')
	
	

def pattern_ddd(x, lc): # pattern to print  [xxx   xxx]
	
	tc = 1 # temp counter
	gc = int(x/3) # gap counter
	p = 1 # phase counter

	hc = 1 # horizontal line counter

	for i in range(x):

		if p%2 != 0:  # horizontal - odd(s)

			if tc <= gc:
				# print("#", end='')
				pattern_ver_xxx_xdd(gc, lc, hc)
				tc+=1
			else: # filled to blank space
				print(" ", end='')
				tc = 2
				p+=1

		
		else:	# horizontal - even(s)
			if tc <= gc:
				print(" ", end='')
				tc+=1
			else: # blank to filled space
				print("#", end='')
				tc = 2
				p+=1

		hc+=1
		# print(i, end='')



def pattern_xxx(x): # pattern to print  [xxxxxxxxx]
	print("#"*x, end='')
	


def pattern_xdd(x): # pattern to print  [.x..x..x.]
	
	c = 1

	for i in range (x):
		if c<2:
			print("#", end='')
			c+=1
		else:
			print(" ", end='')
			c=0



# def mainloop():



def main():
	n = int(sys.argv[1])
	x = 3**n # height / width
	ts = x*x # total number of squares

	tc = 1 # temp counter
	gc = int(x/3) # gap counter
	p = 1 # phase counter



	s = 1 # starting part
	e = x-(x/3)+1 # ending part


	gs = 1 # gap string (x3)
	pc = 2 # pattern counter (x2)


	lc = 1 # carpet's middle section line counter


	if n == 0:
		print("#")
		sys.exit()


	# main loop
	for i in range (1,x+1):

		# The carpet is divided into 3 parts
		# 1 (odd | start) and 3 (odd | end) are same
		# 2 (even | middle) with blank centre

		if p%2 != 0: 

			if tc <= gc:
				if i%2 == 0 :
					pattern_xdd(x)	
				else:
					pattern_xxx(x)

				tc+=1
			else:	# xxx / xdd to ddd (change)
				pattern_ddd(x, lc)
				lc+=1
				tc = 2
				p+=1

		
		else:
			if tc <= gc:
				pattern_ddd(x, lc)
				lc+=1
				tc+=1
			else:	# ddd to xxx (change)
				pattern_xxx(x)
				tc = 2
				p+=1


		print('\t\t', p, tc, gc ,i)

		
	print('\n[', n, x, ts, ']')


  
if __name__ == "__main__":
	main()
