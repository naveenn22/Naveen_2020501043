# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

import math
def isPerfectSquare(n):
	m=int(math.sqrt(n))
	if(m**2 == n):
		return True
	return False
def largestperfectsquare(n):
	# your code goes here
	for i in range(n,0,-1):
		# if(isPerfectSquare(i)):
		# 	return i
		if(math.isqrt(i)**2==i):
			return i