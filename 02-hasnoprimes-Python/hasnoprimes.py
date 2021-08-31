# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	for i in range(len(l)):
		for j in range(len(l[i])):
			if isprime(l[i][j]):
				return False
	return True

		

def isprime(a):
	if (a<2):
		return False
	for i in range(2,a):
		if (a%i==0):
			return False
	return True 
# print(fun_hasnoprimes([[11]]))