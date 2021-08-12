# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
# source: took some logic from Geeksforgeeks

def mostfrequentdigit(n):
	# your code goes here
	
	if (n < 0):
		n = -n
	result = 0 
	max_count = 1 
	
	for d in range(9,-1,-1):
		count = countrepeat(n, d)
		if (count >= max_count):
			max_count = count
			result = d
	return result

	# pass

def countrepeat(x, d):
    count = 0; 
    while (x>0):   
        if (x % 10 == d):
            count += 1
        x = int(x / 10)
 
    return count
 
