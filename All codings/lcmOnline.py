def decimalToBinary(n): 
	if(n > 1): 
		# divide with integral result 
		# (discard remainder) 
		decimalToBinary(n//2) 
	print(n%2, end=' ') 
	
	

decimalToBinary(10)
