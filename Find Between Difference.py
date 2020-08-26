def difference(nums):
    nums.sort()
    return max(nums)-min(nums)

print(difference([10, 15, 20, 2, 10, 6]))

#op:-18