# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().
def getKthDigit(hand):
	count = 0
	while(hand>0):
		rem = hand % 10
		hand = hand // 10
		count += 1
	return count

def handtodice(hand):
	# your code goes here
	# print(hand)
	temp = hand
	res = ()
	numOfDigits = getKthDigit(hand)
	while(numOfDigits>0):
		temp = hand // 10**(numOfDigits - 1)
		hand = hand % 10**(numOfDigits - 1)
		res+= (temp, )
		numOfDigits-=1
		
		# hand = hand // 10
		# temp = hand
	return res
	pass

# print(handtodice(int(input())))
