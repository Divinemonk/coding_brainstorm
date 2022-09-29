# Algorithm :scroll:


### Variables
```
n   :  User entered number
c   :  Counter value, iterates till n
p   :  Stores main (formatted) pattern
tp  :  Temporarily stores (unformatted) pattern
```

### Shortcuts
```
\s  :  Blank space
x3  :  Print previous mentioned string trice (3 times)

(first line, only line)  :  Pattern has only one line
(line by line)		 :  Pattern has multiple lines, extract each line and use
(line - space - line)	 :  Pattern has multiple lines, extract each line and use with [pattern - space - pattern]
```


### Main ___algo___ :eight_pointed_black_star:
```
n = user enters 2


stores pattern when (c)n=0
	tp =  single '#'
	p = tp


stores pattern when (c)n=1
	tp =               'p' x3 		  (first line, only line)
		  	   'p' '\s' 'p' 
		  	   'p' x3		  (first line, only line)
	p = tp


stores pattern when (c)n=2
	tp =               'p' x3 		           (line by line)
		           'p' '\s' 'p' 	    (line - space - line)
		  	   'p' x3		           (line by line) 
	p = tp (if n>2)

```

<br><br>


### Test cases `n =2 & >2`, have same algo
Example (for n=3):
```
tstores pattern when (c)n=3
	tp =              'p' x3 		           (line by line)
		          'p' '\s' 'p' 	            (line - space - line)
		  	  'p' x3		           (line by line) 
```
Note: here algo is same as it was for `n=2`



<br><br>

> [Go Back](./solutions.md) (solutions menu)

> [Go Back](./README.md) (question page)
