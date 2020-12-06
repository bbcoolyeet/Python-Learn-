import collections
def numS_countwr(n):
    x = [int(d) for d in str(n)]
    occurrences = collections.Counter(x)
    print(occurrences)
n = 43365644
numS_countwr(n)