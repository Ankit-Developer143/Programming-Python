#lambda

# lambda arguments : expression

x = lambda a:a+10
print(x(10)) #op:-20

x = lambda a,b: a+b
print(x(2,2))
#op:-4

def add(n):
    return lambda a: a*n

doubler = add(2)
print(doubler(3))
#op:-6



