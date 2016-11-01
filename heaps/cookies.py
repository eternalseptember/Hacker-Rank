"""
Jesse loves cookies. He wants the sweetness of all his cookies to
be greater than value K. To do this, Jesse repeatedly mixes two
cookies with the least sweetness. He creates a special combined
cookie with:

sweetness = (1 x Least sweet cookie + 2x 2nd least sweet cookie)

He repeats this procedure until all the cookies in his collection
have a sweetness >=K. You are given Jesse's cookies. Print the
number of operations required to give the cookies a sweetness >= K.
Print -1 if this isn't possible.

Input Format:
The first line consists of integers N, the number of cookies and K,
the minimum required sweetness, separated by a space.
The next line contains N integers describing the array A where A is
the sweetness of the ith cookie in Jesse's collection.

Output Format:
Output the number of operations that are needed to increase the
cookie's sweetness >= K. Output -1 if this isn't possible.
"""


def cookies_arrange(list):
	#





#n, k = (int(temp) for temp in input().split(' '))
#cookies = [int(temp) for temp in input().split(' ')]

in_1 = '6 7'
in_2 = '1 2 3 9 10 12'

n, k = (int(temp) for temp in in_1.split(' '))
cookies = [int(temp) for temp in in_2.split(' ')]

num_of_opers = cookies_arrange(cookies)
print(num_of_opers)
