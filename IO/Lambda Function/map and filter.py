#filter:-function:iterable
#map:-function : iterable

#lambda:-parameter :expression
#filter

# nums = [1,2,3,4,5]
# even = list(filter(lambda a:a%2==0,nums))
# print(even)
#(2,4)

nums = (1,2,3,4,5)
result = list(map(lambda n:n*2,nums))
print(result)
#op: [2, 4, 6, 8, 10]

nums = (1,2,3,4,5)
result = list(filter(lambda n:n*2,nums))
print(result)
#op:-[1, 2, 3, 4, 5]



#list and tuple list[]   and tuple()




    


