mylist1 = [1,2,3,4,5,6,7]
mylist2 = [8,9]


"""Concatination """
result = mylist1+mylist2
print(result)
#op:- [1,2,3,4,5,6,7,8,9]


"""Append List"""
#mylist1.append(mylist2) 

#op:-[1, 2, 3, 4, 5, 6, 7, [8, 9]]


"""Extend List"""
mylist1.extend(mylist2)
print(mylist1)
#op:-[1, 2, 3, 4, 5, 6, 7, 8, 9]


"""Length of List"""
print(len(mylist1))
#op:-9


"""Slicing"""
print(mylist1[0:4])
#op:-[1, 2, 3, 4]

"""reverse"""
mylist1.reverse()
#op:;-[9, 8, 7, 6, 5, 4, 3, 2, 1]
print(mylist1)




""" Accessing This Dual List (Nested)"""

mylist4 = [1,2,3,4,5,['x','y','z']]

print(mylist4[5])
#op:-['x', 'y', 'z']

print(mylist4[5][2])
#op:-z

print(mylist4[0])
#op:-1


"""List Comprehesion"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = [row[0] for row in matrix]
print(result)


