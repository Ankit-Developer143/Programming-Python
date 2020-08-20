def difference_max_min(lst):
    lst.sort()
    print(lst[-1] - lst[0])

difference_max_min([10, 4, 1, 4, -10, -50, 32, 21])



""" Question 


difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32."""