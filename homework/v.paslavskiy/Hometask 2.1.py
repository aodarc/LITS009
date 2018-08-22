lst = [1, [2, 3], 4, [[6, 7]]]

def list_merge(lst):
  lst2 = []
  for a in lst:
    if isinstance(a, list):
        lst2.extend(list_merge(a))
    else:
        lst2.append(a)
  return lst2

lst2 = list_merge(lst)
print(lst2)