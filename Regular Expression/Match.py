""" After you've defined a regular expression, 
the re.match function can be used to determine whether it matches at the beginning of a string. 

To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".


The function re.findall returns a list of all substrings that match a pattern.
"""

import re

pattern = r"spam"

if re.match(pattern,"spamspamspam"):
    print("Match")
else:
    print("Not Match")


#op:- Match


""" re.search The function re.search finds a match of a pattern anywhere in the string. """

patterns = r"spam"

if re.search(patterns,"iffispamfh9fhh"):
    print("Match")
else:
    print("Not Match")
    
#Match

print(re.findall(pattern, "eggspamsausagespam"))
#op:-['spam', 'spam']