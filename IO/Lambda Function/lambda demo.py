
add  = lambda a,b: a+b
print(add(2,2))

#Single Expression
result = lambda x:x%2==0 and True or False
print(result(4))


result = lambda *args:args*2
print(result(10,20,30))
#op:- (10, 20, 30, 10, 20, 30)