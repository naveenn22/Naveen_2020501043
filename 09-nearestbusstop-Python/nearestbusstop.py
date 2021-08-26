# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	if(street<5):
		return 0
	if(street%8==0):
		return street
	a=str(street/8)
	b=a.split('.')
	b[1]=b[1][::-1]
	c=int(b[1])%10
	if(c>5):
		return int(b[0])*8+8
	else:
		return int(b[0])*8
