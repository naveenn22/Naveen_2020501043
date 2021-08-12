# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	n = int(n * 10)
	round_digit = int(n % 10)
	k = n // 10
	# print(n)
	# print(k)
	if(round_digit>=5):
		
		if(k%2 == 0):
			return int(k+1)
		else:
			return int(k)
	else:
		if(k%2 == 0):
			return int(k-1)
		else:
			return int(k)
		 


	# return round_digit

# print(fun_nearestodd(12.0))