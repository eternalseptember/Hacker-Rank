"""
There are N strings. Each string's length is no more than 20 characters.
There are also Q queries. For each query, you are given a string, and
you need to find out how many times this string occurred previously.

Input Format:
The first line contains N, the number of strings.
The next N lines each contain a string.
The N + 2nd line contains Q, the number of queries.
The following  lines each contain a query string.
"""

N = int(input().strip())
strings = []
for i in list(range(N)):
	strings.append(input())

Q = int(input().strip())
for i in list(range(Q)):
	query = input()
	occurances = strings.count(query)
	print(occurances)
