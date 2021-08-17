# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	# Your code goes here
	if n==0:
		return 1
	l=[1]
	i=1
	while(len(l)<=n):
		a=fact(i)
		print(a)
		b=squares(a,i)
		if b==True:
			l.append(i)
		i+=1
	return l[n]

def fact(n):
	l=[]
	for i in range(2,n):
		if n%i==0:
			if(prime(i)):
				l.append(i)
	return l

def squares(l,n):
	if len(l)==0:
		return False
	for i in l:
		if n%(i**2)!=0:
			return False
	return True


def prime(a):
	if (a<2):
		return False
	for i in range(2,a):
		if (a%i==0):
			return False
	return True

	# pass
print(nthpowerfulnumber(5))