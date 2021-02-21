def missing(input_arry):
    input_arry = [t for t in input_arry if t!= 0]
    x = len(input_arry)
    total = (x + 1)*(x + 2)/2
    final_clac = sum(input_arry)
    totalcalc = total - final_clac
    return totalcalc
input_arry = [0,1,2,3,6,4,0]    
print(missing(input_arry))