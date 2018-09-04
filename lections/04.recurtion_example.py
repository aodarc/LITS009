def make_flat(lst):
	result = []

	for l in lst:
		if isinstance(l, list):
			result.extend(make_flat(l))
		else:
			result.append(l)
	return result

l = [1,2,3, [5,4, [7]], [8,9]]

print(make_flat(l))