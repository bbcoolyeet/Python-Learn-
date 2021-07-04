def recursion(number):
    if number < 10:
        return number    
    div = number % 10
    return div + recursion(number//10)
    
number = 58921
print(recursion(number))
