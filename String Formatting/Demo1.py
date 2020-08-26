nums = [4,5,6]
msg = {"The Number is {0} {1} and {2}" .format(nums[0],nums[1],nums[2])}
print(msg)

#op:-{'The Number is 4 5 and 6'}

obj = {"Hello My First Name is {a} and Last Name is {b} ".format(a = 'Ankit' , b = 'Singh')}
print(type(obj)) #Set
print(obj) #{'Hello My First Name is Ankit and Last Name is Singh '}


print("{0}{1}{0}".format("abra", "cad"))
#op:-abracadabra