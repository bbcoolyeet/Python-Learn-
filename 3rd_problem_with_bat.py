def batseq(firststr, secondstr):
  if len(secondstr) ==0:
    return True
  if len(firststr) ==0 and len(secondstr)>0:
    return False
  if secondstr[0] == firststr[0]:
    return batseq(secondstr[1:], firststr[1:])
  else:
    return batseq(secondstr, firststr[1:])
firststr = 'table'
secondstr = 'bat'
print(batseq(firststr, secondstr))