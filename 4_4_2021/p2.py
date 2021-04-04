def mono(placeholder):
    anotherplaceholdervalue = placeholder[0]
    if placeholder[0] > placeholder[-1]:
        for j in range(len(placeholder) - 1):
            if placeholder[j] < placeholder[j+1]:
                return False
        return True
    for i in placeholder:
        if i < anotherplaceholdervalue:
            return False
        anotherplaceholdervalue = i
    return True
    
placeholder = [1,2,4,5]
print(mono(placeholder))