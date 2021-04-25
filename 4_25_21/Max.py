def sortedlst(nums):
    """
    >>> sortedlst([1,2,3])
    6
    >>> sortedlst([2,5,7,2,6,4,8])
    56
    >>> sortedlst([-13,-10,-5,-1,0])
    130
    """

    sortednums = sorted(nums)
    x = sortednums[-1]
    y = sortednums[-2]
    z = sortednums[0]
    u = sortednums[1]
    if x*y >= z*u:
        return x*y
    else: 
        return z*u
nums = [-11,-12,6,2,9]
print(sortedlst(nums))
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
