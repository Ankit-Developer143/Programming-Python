
#String

myStr = 'abcdef'
print(myStr[0])
print(myStr[1])
print(myStr[2])
print(myStr[3])
print(myStr[-1])
""" 
op:-
a
b
c
d 
f
"""

#Indexing

myStr1 = 'abcdef'
print(myStr1[1:])#bcdef

print(myStr1[:2])#ab

print(myStr1[1:2])#b



#Slicing

myStr2 = 'abcdef'

print(myStr2[: :2])#ace


#Split
MyStr3 = 'a,b,c,d'

print("This is the Split Methods",MyStr3.split("a"))


print(type(MyStr3.split()))

""" 

This is the Split Methods ['', ',b,c,d']
<class 'list'> 
"""

#.format

x = "item one: {} Item two: {} ".format("a","b")
x1 = "item one: {a} Item two: {b} ".format(a="vegitable",b = "Mango")
print(x)#item one: a Item two: b
print(x1)#item one: vegitable Item two: Mango






