"""
Details and a Twist:
You will be given a list that contains both integers and strings.
Can you print the strings in order of their accompanying integers?
If the integers for two strings are equal, ensure that they are
print in the order they appeared in the original list.

The Twist - Your clients just called with an update. They don't
want you to print the first half of the original array. Instead,
they want you to print a dash for any element from the first half.

Input Format:
- n, the size of the list ar.
- n lines follow, each containing an integer x and a string s.

Output Format:
Print the strings in their correct order.

"""



"""
n = int(input().strip())
arr = []
for i in range(n):
	x, s = input().strip().split(' ')

"""


# Setting up test case 1:
# - - - - - to be or not to be - that is the question - - - -

n = 20
in_str1 = ['0 ab', '6 cd', '0 ef', '6 gh', '4 ij', '0 ab', '6 cd', '0 ef', '6 gh', '0 ij', '4 that', '3 be', '0 to', '1 be', '5 question', '1 or', '2 not', '4 is', '2 to', '4 the']



