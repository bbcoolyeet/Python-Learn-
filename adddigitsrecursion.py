def recursion(number):
    if number > 0:
        div = number % 10
        return div + recursion(number//10)
    return 0
number = 58921
print(recursion(number))