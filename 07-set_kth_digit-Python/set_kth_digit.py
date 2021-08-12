# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

# def getKthDigit(n, k):
	


def fun_set_kth_digit(n, k, d):
	count = 1
	res = 0 
	flag=False
	if(n>0):
		while(n>0):
			
			temp = n % 10
			n = n//10
			if(count==k+1):
				# print(res)
				
				res += d*(10**(count-1))
				flag = True
				# print(res)
			else:
				res += temp*(10**(count-1))
				# print(res)
			count+=1
		# print(count)
		# print(k)	
		# # print("*********************")
		# if(count>k):
		# 	res+=d*(10**(count-1))
		if(flag == False):
			res += d*(10**(count-1))
		return res
	else:
		count=1
		num = abs(n)
		s="1" + str(num)
		n = int(s)
		# print(s)
		# print(100)
		# print(n)
		while(n>0):
			
			temp = n % 10
			n = n//10
			if(count==k+1):
				# print(res)
				
				res += d*(10**(count-1))
				# print(res)
			else:
				res += temp*(10**(count-1))
				# print(res)
			
			count+=1
		# print("*********************")
		return int(-res)
			
print(fun_set_kth_digit(468, 0, 1,))		
print(fun_set_kth_digit(468, 1, 1))	
print(fun_set_kth_digit(468, 2, 1))	
print(fun_set_kth_digit(468, 3, 1  ))	
print(fun_set_kth_digit(-468, 3, 1))	

