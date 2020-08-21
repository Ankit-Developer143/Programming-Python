# Tuples

t = (1, 2, 3)
print(t)
#op:-(1, 2, 3)

print(t[2])
# op:-3

""" 
t['item'] = 'food'
print(t) """       """ Tuple Are Immutable (Not Change) """


# Set

""" Unorder Collection of Unique Element """

x = set("Ankit")
print(x)  # op:-{'i', 'n', 'k', 't', 'A'}
print("pop The Values", x.pop())  # op:-i


y = set()
y.add(10)
y.add(20)
y.add(30)
y.add(0.1)
y.add(2.0)
y.add(2.0)

print(y)
#op:-{2.0, 10, 0.1, 20, 30}
""" Not Accept Duplicate Values """


#print("Pop The Values",y.pop())
