#Change All The Char in lowercase



def match(s1, s2):
    if s1.casefold() == s2.casefold():
        return True
    else:
        return False
print(match("hello", "hELLo"))
    
#True