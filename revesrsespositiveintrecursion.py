def recursenum(number):
    while (number > 0):  
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10  
revs_number = 0    
number = 5  
recursenum(number)
