#!/usr/bin/python
# Sierpinski Carpet (v2)
# A Divinemonk creation!


import sys

n = int(sys.argv[1])
c=0
p = '█' # pattern variable
tp = '' # temp pattern variable


while(c<n):

	if c < 1: # (c)n = 1
		tp = p*3+'\n' + p+' '+p+'\n' + p*3+'\n'
		p=tp

	if c >= 1: #(c)n =/> 2
		tp2 = ''
		tp=''

		for l in p.splitlines():
			tp += l*3+'\n'
			tp2 += l + ' '*len(l) + l + '\n'

		p = tp + tp2 + tp 

	c+=1

  
print(p)
