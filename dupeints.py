def dupefind(arrays):
    
    empty_arr = []
    for i in arrays:
        if i not in empty_arr:
            return True
        empty_arr.append(i)
    return False


arrays = [0,1]
print(dupefind(arrays))
