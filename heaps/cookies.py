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
The next line contains N integers describing the array A where A_i
is the sweetness of the i-th cookie in Jesse's collection.

Output Format:
Output the number of operations that are needed to increase the
cookie's sweetness >= K. Output -1 if this isn't possible.
"""


def cookies_arrange(cookies, min_sweetness):
	cookies_list = cookies[:]
	cookies_list.sort()

	steps = 0
	while (cookies_list[0] < min_sweetness):
		cookie1 = cookies_list.pop(0)
		cookie2 = cookies_list.pop(0)
		new_cookie = cookie_formula(cookie1, cookie2)
		cookies_list.append(new_cookie)
		cookies_list.sort()
		steps += 1

		if len(cookies_list) == 1:
			break

	if cookies_list[0] >= min_sweetness:
		return steps
	else:
		return -1


def cookie_formula(cookie_1, cookie_2):
	return (1 * cookie_1 + 2 * cookie_2)




#n, min_sweetness = (int(temp) for temp in input().split(' '))
#cookies = [int(temp) for temp in input().split(' ')]

in_1 = '6 7'
in_2 = '1 2 3 9 10 12'

n, min_sweetness = (int(temp) for temp in in_1.split(' '))
cookies = [int(temp) for temp in in_2.split(' ')]

num_of_opers = cookies_arrange(cookies, min_sweetness)
print(num_of_opers)
