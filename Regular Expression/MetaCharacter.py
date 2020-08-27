""" Metacharacters

The first metacharacter we will look at is . (dot).
This matches any character, other than a new line.
 """
import re
pattern = r"gr.y"

if re.match(pattern,"grey"):
   print("Match")

if re.match(pattern,"gray"):
   print("Match")
   
   
""" 
op:-
Match
Match """




                
""" Metacharacters

The next two metacharacters are ^ and $.
These match the start and end of a string, respectively.
Example: """

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   prit("Match 3")
   
""" 
OP:-
Match1
Match2 """


pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")  
   
#op:- Match 1





                 
""" Character Classes

Character classes can also match ranges of characters.
Some examples:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit.
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
Example:
 """    

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")
   
""" 
op:-
Match

 """
   
   