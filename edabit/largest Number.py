def findLargestNum(nums):
    nums.sort()
    return(nums[-1])
        
print(findLargestNum([4, 5, 1, 3]))
