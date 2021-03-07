def dupefind(arrays):
    
    empty_arr = []
    for i in arrays:
        if i in empty_arr:
            return True
        else:
            empty_arr.append(i)
    return False


arrays = [0,1, 1]
print(dupefind(arrays))
