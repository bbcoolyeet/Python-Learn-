def display(n):
    if(n > 1):
        display(n-1)
    print('hello python')
n = int(input('how many'))
display(n)