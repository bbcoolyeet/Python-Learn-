# #Given three numbers x, y and m where 1 <= x < y <= m, use x and y to compose the largest possible number that is <=m. You can use any number of x and y.
# For instance, when x=17, y=25, and m=77, the output will be 76 because 17*3 + 25*1 = 76 and you can't compose 77 with 17 and 25.
# Think about how you solve this problem mathematically and then convert the thought process into code.
import math
def biggest_combo_in_3_nums(x,y,m):
    max = 0

    for howmany_y in range(0 ,m//y + 1):
        howmany_x = y//x
        added = howmany_x * x + howmany_y * y
        if max <= added:
            max = added
    return max

# def closest_num(nums, k):
#     max = -math.inf
#     for i in nums:
#         if i >= max and i <= k:
#             max = i
#     return max


# def maxnums(nums):
#     max = -math.inf
#     for i in nums:
#         if i > max:
#            max = i
#     return max


# k = 5
# nums = [9,3,4,8]
x = 17
y = 25
m = 77
print(biggest_combo_in_3_nums(x,y,m))