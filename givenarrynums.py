import collections
def find_third_largest_num(nums):
    """
    >>> find_third_largest_num([2, 2, 4, 4, 5])
    4
    >>> find_third_largest_num([1, 2, 4, 6])
    2
    """
    sortednums = sorted(nums)
    if len(sortednums) < 3:
        return sortednums[-1]
    return sortednums[-3]
    #good_sort = [item for item, count in collections.Counter(sortednums).items() if count >= 1]
    
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)