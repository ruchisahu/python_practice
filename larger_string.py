#could the string be empty?
#could the number be negative
#what if they are same number

#solution:first compare length
#if same length compare char by char

def larger_string(a,b):
	if len(a)>len(b):
		return True
	elif len(a)<len(b):
	    return False
	for i in range(len(a)):
	    if a[i]==b[i]:
	    	continue
	    elif a[i]>b[i]:
	    	return True
	    else:
	    	return False
	return False    	

	 	
print(larger_string("112","111"))

print(larger_string("11","1"))

print(larger_string("1","1"))

print(larger_string("","1"))

