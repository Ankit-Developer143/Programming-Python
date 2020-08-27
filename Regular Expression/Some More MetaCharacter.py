""" Metacharacters

Some more metacharacters are *, +, ?, { and }.
These specify numbers of repetitions.
The metacharacter * means "zero or more repetitions of the previous thing". 
It tries to match as many repetitions as possible.
 The "previous thing" can be a single character, a class, or a group of characters in parentheses """
 
import re

pattern = r"egg(spam)*"  #More Repition

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")
   
""" 
op:-
Match 1
Match 2 """



""" The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".
Example: """


pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")
   
""" 
op:-
Match 1
Match 2 """



""" 
Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something".
Hence {0,1} is the same thing as ?.
If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
Example: """


pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")
if re.match(pattern, "9999"):
   print("Match 3")


""" 
op:-
Match 1
Match 2
 """
 
 
 
""" Groups

The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.
Example: """


pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())
   
   
""" 
abcdefghi
abcdefghi
bc
de
('bc', 'de', 'fgh', 'g') """