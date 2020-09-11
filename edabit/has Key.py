def has_key(dictionary, key):
    if key in dictionary.keys():
        return True
    else:
        return False
    
print(has_key({ "a": 44, "b": 45, "c": 46 }, "b"))

//True