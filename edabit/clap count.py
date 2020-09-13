 # Count Loops
 def count_claps(txt):
 	return txt.count('C')
print(count_claps("ClaClaClaClap!"))
 #op:-4

#Using For Loops
def count_claps(txt):
    counter = 0
    for char in txt:
        if char == 'C':
            counter += 1
    return counter
print(count_claps("ClaClaClaClap!"))
#op:-4

#Lambda Function
result = lambda txt:txt.count('C')
print(result("ClaClaClaClap!"))

