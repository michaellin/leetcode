def diffArrays(la, lb):
	#if (len(a) > len(b)):
	lookup_int = {}
	for a in la:
		if not a in lookup_int:
			lookup_int[a] = 1
		else:
			lookup_int[a] += 1

	diff_la = []
	diff_lb = []
	common = []
	for b in lb:
		if (b in lookup_int):
			if (lookup_int[b] > 0):
				# have a common element
				lookup_int[b] -= 1
				common += [b]
			else:
				diff_lb += [b]
		else:
			diff_lb += [b]

	for a in la:
		if a not in common:
			diff_la += [a]

	return (diff_la, diff_lb)


la = [2,9,2,1]
lb = [3,1,2]
print(diffArrays(la, lb))

# {1: 0, 2: 0, 3:0}
# lb = []
# 4