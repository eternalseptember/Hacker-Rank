"""
Given N, Q, and Q queries, execute each query.

Input Format:
The first line contains two space-separated integers, N (the number
of sequences) and Q (the number of queries), respectively.
Each of the Q subsequent lines contains a query in the format defined above.
"""


# n, q = (int(temp) for temp in input().split(' '))
str = '2 5'
n, q = (int(temp) for temp in str.split(' '))

seqList = [[] for i in range(n)]
lastAns = 0

test_seq = ['1 0 5', '1 1 7', '1 0 3', '2 1 0', '2 1 1']

for i in range(q):
	# queryType, x, y = (int(temp) for temp in input().split(' '))
	queryType, x, y = (int(temp) for temp in test_seq[i].split(' '))

	index = (x ^ lastAns) % n
	seq = seqList[index]

	if queryType == 1:
		seqList[index].append(y)
	else:
		size = len(seq)
		element = y % size
		lastAns = seq[element]
		print(lastAns)
