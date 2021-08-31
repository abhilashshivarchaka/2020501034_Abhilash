# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.


def isnum(n):
	# l=['0','1','2','3','4','5','6','7','8','9']

	x=n**5
	l=[]
	while x>0:
		a=x%10
		l.append(a)
		x=x//10

	for i in range(10):
		if(i not in l):
			return False
	return True

n=474
print(isnum(n))


def nthwithproperty309(n):
	# Your code goes here
	found = 1
	guess = 0
	while(guess<=n):
		# guess+=1
		if(isnum(found)==True):
			guess+=1
		found+=1	
	return found-1

print(nthwithproperty309(1))