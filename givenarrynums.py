import collections
def intnums(nums):
    sortednums = sorted(nums)
    
    
    good_sort = [item for item, count in collections.Counter(sortednums).items() if count >= 1]
    if len(good_sort) < 3:
        return good_sort[-1]
    else: 
        for i in range(0,2):
            sortednums = max(nums)
            nums = [t for t in nums if t!= sortednums]
        maxnum = max(nums)
        return maxnum
    
nums = [2,4,2,2,4,2,2,4]
print(intnums(nums))