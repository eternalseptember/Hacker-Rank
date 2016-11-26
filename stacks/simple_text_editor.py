"""
In this challenge, you must implement a simple text editor.
Initially, your editor contains an empty string, S. You must
perform Q operations of the following 4 types:

1. append(W) - Append string W to the end of S.
2. delete(k) - Delete the last k characters of S.
3. print(k) - Print the kth character of S.
4. undo() - Undo the last (not previously undone) operation of
type 1 or 2, reverting  to the state it was in prior to that
operation.
"""


# q = int(input().strip())

q = 8
in_str = ['1 abc', '3 3', '2 3', '1 xy', '3 2', '4 ', '4 ', '3 1']

S = ''
oper_list = []

for i in range(q):
	# oper = input().strip()
	oper = in_str[i].strip()

	try:
		op, k = oper.split(' ')
	except:
		op = oper

	if op == '1':
		oper_list.append(len(S))
		S += k
	elif op == '2':
		delete = S[-int(k):]
		oper_list.append(delete)
		S = S[:-int(k)]
	elif op == '3':
		print(S[int(k) - 1])
	else:
		undo = oper_list.pop()
		if type(undo) == int:
			# undo last append operation
			S = S[:int(undo)]
		else:
			# undo last delete operation
			S += undo





