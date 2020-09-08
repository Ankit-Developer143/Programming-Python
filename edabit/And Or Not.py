def NOT(num):
	if num == 1:
		return 0
	return 1
print(NOT(1))

#op:-0	
 	
def AND(num,num2):
	if num == num2 == 1:
		return 1
	return 0
print(AND(1,0))
	
 #op:-1
 	
def OR(num,num2):
	if num == num2 == 0:
		return 0
	return 1

print(OR(1,1))

#op:-1