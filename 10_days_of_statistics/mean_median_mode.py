"""
Given an array, X, of N integers, calculate and print the the respective mean,
median, and mode on separate lines. If your array contains more than one modal
value, choose the numerically smallest one.

Your answers should be in decimal form, rounded to a scale of 1 decimal place.
"""


from collections import Counter


# N = int(input().strip())
# arr = [int(temp) for temp in input().strip().split(' ')]

# Test case 1:
# Expected answer: 43900.6  44627.5  4978
N = 10
in_str1 = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'
arr = [int(temp) for temp in in_str1.strip().split(' ')]


# mean
total = 0
for num in arr:
	total += num
mean = total / N
print('{0:.1f}'.format(mean))


# median
arr.sort()
med_index = N // 2
if N % 2 == 0:
	# average out the two middle numbers
	total = arr[med_index - 1] + arr[med_index]
	print('{0:.1f}'.format(total / 2))
else:
	print('{0}'.format(arr[med_index]))


# mode
mode = Counter(arr).most_common(1)
print(mode)


