Problem:find the second largest number in array.
#questions:could this array be empty
#Could this array have only one element
#in case of two max element-551 (return 5)
def second_largest(array):
	largest=None
	second_largest=None
	for curr in array:
		if largest==None:
			largest=curr
		elif curr>largest:
			 second_largest=largest
			 largest=curr
		elif second_largest==None:
		     second_largest=curr
		elif curr>second_largest:
		     second_largest=curr
	return second_largest	          	 






#case1
print(second_largest([1,3,4,5,1,3,0]))

#case2-negative numbers
print(second_largest([-1,-2,-3,-6,-3]))

#case3-1 element should return none
print(second_largest([1]))

#case4-blank list
print(second_largest([]))