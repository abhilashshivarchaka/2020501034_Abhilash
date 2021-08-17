# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l): 
	if len(l)==0:
		return 0
	else:
		return(added(l,0,0))
	
def added(l,i,a):
	if(i>=len(l)):
		return a
	else:
		if(i%2==0):
			a+=l[i]
		else:
			a-=l[i]
	return added(l,i+1,a)







	# s=0
	# for i in range(len(l)):
	# 	if i%2==0:
	# 		s+=l[i]
	# 	else:
	# 		s-=l[i]

	# return s