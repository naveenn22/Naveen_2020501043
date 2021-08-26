# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
	m=int(math.sqrt(pow(b,2)-(4*a*c)))
	res1=int(((-b)+m)/(2*a))
	res2=int(((-b)-m)/(2*a))
	if(res1>res2):
		res1,res2=res2,res1

	return res1,res2


