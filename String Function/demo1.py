obj = "Hello World"



#Split
result =obj.split(" , ")
print(result)
#op:-['Hello', 'World']


#replace 

obj1 = "Hello World"
res = obj1.replace("World","Country")
print(res)
#op:-Hello Country

#Startswith and endswith

check = obj1.startswith("H")
check1 = obj1.endswith("World")
print(check) #True
print(check1) #True 


"""Join"""

print(", ".join(["spam", "eggs", "ham"]))
#op: type str
# op:  spam, eggs, ham


a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)
