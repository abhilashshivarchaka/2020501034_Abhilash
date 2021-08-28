# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.




def fun_getaverage(s):
	a=s.split(",")
	sum=0
	count=0
	
	for  i in a:
		if i.isnumeric():
			sum+=int(i)
			count+=1
			print(i)
	if count==0:
		return 0
	avg=sum/count
	
	return avg
print(fun_getaverage('13,excused,14,absent'))
