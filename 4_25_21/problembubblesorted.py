def sortedlst(nums):
    
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
nums = [-11,-12,6,2,9]
print(sortedlst(nums))
