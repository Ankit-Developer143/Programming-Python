from itertools import product, permutations

#Show Possibility

letters = ("A", "B")
print(list(product(letters, range(2))))
#print(permutations(letters)) #<itertools.permutations object at 0x051E8370>
print(list(permutations(letters)))