"""
You have three stacks of cylinders where each cylinder has the same
diameter, but they may vary in height. You can change the height of
a stack by removing and discarding its topmost cylinder any number
of times.

Find the maximum possible height of the stacks such that all of the
stacks are exactly the same height. This means you must remove zero
or more cylinders from the top of zero or more of the three stacks
until they're all the same height, then print the height. The
removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format:
The first line contains three space-separated integers, n1, n2, and
n3, describing the respective number of cylinders in stacks 1, 2, and
3. The subsequent lines describe the respective heights of each
cylinder in a stack from top to bottom:

The second line contains n1 space-separated integers describing the
cylinder heights in stack 1.
The third line contains n2 space-separated integers describing the
cylinder heights in stack 2.
The fourth line contains n3 space-separated integers describing the
cylinder heights in stack 3.
"""


def FindHeight(stack1, stack2, stack3):
	# Initializing...
	stacks = []
	heights = []
	for stack in [stack1, stack2, stack3]:
		stack.reverse()
		stacks.append(stack)
		heights.append(totalHeight(stack))

	matching = False
	while matching is False:
		heights = [totalHeight(stack) for stack in [stack1, stack2, stack3]]
		# print('Heights: {0}'.format(heights))
		tallest = max(heights)
		howMany = heights.count(tallest)
		# print('Tallest: {0}  How Many? {1}'.format(tallest, howMany))

		if howMany == 3:
			matching = True
		else:
			tallestIndex = heights.index(tallest)
			# print(stacks)
			stacks[tallestIndex].pop()

	return tallest


def totalHeight(stack):
	height = 0
	for item in stack:
		height += item
	return height



line1 = '5 3 4'
line2 = '3 2 1 1 1'
line3 = '4 3 2'
line4 = '1 1 4 1'

# n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = line1.strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]

# h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
# h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
# h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
h1 = [int(h1_temp) for h1_temp in line2.strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in line3.strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in line4.strip().split(' ')]


height = FindHeight(h1, h2, h3)
print(height)

