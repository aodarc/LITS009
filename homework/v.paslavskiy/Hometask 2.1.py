lst = [1, [2, 3], 4, [[6, 7]]]

lst2=[]

for a in lst:
  if isinstance(a, list):
    for b in a:
      if isinstance(b, list):
        for c in b:
          lst2.append(c)
      else:
        lst2.append(b)
  else:
    lst2.append(a)
