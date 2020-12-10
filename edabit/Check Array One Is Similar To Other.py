def check_equals(lst1, lst2):
	if (lst1[::] == lst2[::]):
		return True
	else:
		return False
print(check_equals([1, 2], [1, 3]) )
#False