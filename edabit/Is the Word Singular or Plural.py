def is_plural(word):
    if(word.endswith("s")):
        return "plural"
    else:
        return "singular"
print(is_plural("names"))