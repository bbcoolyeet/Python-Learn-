def recursion(howmanytimes):
    if howmanytimes > 1:
        recursion(howmanytimes-1)
    print('hello python')
howmanytimes = int(input('how many time? '))
recursion(howmanytimes)