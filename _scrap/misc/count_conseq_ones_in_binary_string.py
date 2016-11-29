def count_conseq_ones(string):
	max_conseq = 0
	conseq = 0
	for char in string:
		if char == '1':
			conseq += 1
		else:
			conseq = 0

		if conseq > max_conseq:
			max_conseq = conseq
	return max_conseq


n = int(439)
binstring = "{0:b}".format(n)
print(binstring)
print(count_conseq_ones(binstring))
