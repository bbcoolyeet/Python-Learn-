from collections import Counter
import collections
import math
def largest_only_once(nums):
    """
    >>> largest_only_once([])
    -1
    >>> largest_only_once([1,1])
    -1
    >>> largest_only_once([1,2,2,3,4,4])
    3
    """
    counter = Counter(nums)
    max_value_once = -math.inf
    for c, occurs in counter.items():
        if c > max_value_once and occurs == 1:
            max_value_once = c
    if max_value_once == -math.inf:
        max_value_once = -1
    return max_value_once



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)