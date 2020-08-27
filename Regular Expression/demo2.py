""" These methods include group which returns the string matched,
 start and end which return the start and ending positions of the first match, 
 span which returns the start and end positions of the first match as a tuple.
 """


import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())
   
   
   
""" 
op:-
pam
4
7
(4, 7) 
"""



#Search And Replace


str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str) #re.sub(old,new,str)
print(newstr)

#My name is Amy. Hi Amy.

