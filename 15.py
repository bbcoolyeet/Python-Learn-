def num_reverse(num):
    plce_hold = 0
    while(num > 0):
        x = num % 10
        plce_hold = (plce_hold * 10) + x
        num = num//10
    return ("revers is {}".format(plce_hold))
num = int(input("numero"))
print(num_reverse(num))
