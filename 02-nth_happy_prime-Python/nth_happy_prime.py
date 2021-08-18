# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_prime(n):
	# return 0


# def nth_happy_number(n):
	found = 0
	guess = 0
	while(found<=n):
		guess+=1
		if(ishappynumber(guess)):
			if(prime(guess)):
				found+=1
	return guess
def ishappynumber(n):
	# your code goes here
	if(n==1 or n==7):
		return True
	while (n>=10):
		n=squares(n)
		if(n==1):
			return True
	return False

def squares(n):
	s= 0
	while(n):
		s+= (n % 10) * (n % 10)
		n = int(n / 10)
	return s

def prime(a):
	if (a<2):
		return False
	for i in range(2,a):
		if (a%i==0):
			return False
	return True