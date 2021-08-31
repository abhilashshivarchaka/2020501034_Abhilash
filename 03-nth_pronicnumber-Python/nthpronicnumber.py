# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
	a=1
	c=0
	while a<=n:
		c+=1
		if pronicnumber(c):
			a+=1
	return c



	
def pronicnumber(n):
    f=0
    for i in range(n):
        if i *(i+1)==n:
            f=1
            break
    return f==1
