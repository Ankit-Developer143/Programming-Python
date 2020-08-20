def to_int(txt):
    result = str(txt)
    print(type(result))
    return result


def to_str(num):
    res = int(num)
    print(type(res))
    return res


print(to_int("77"))
print(to_str(77))


""" op:-<class 'str'>
77
<class 'int'>
77 """
