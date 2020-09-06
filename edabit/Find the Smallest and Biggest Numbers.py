def min_max(nums):
    nums.sort()
    return [nums[0], nums[len(nums)-1]]
    
print(min_max([2334454, 5]))

#op:-[5, 2334454]