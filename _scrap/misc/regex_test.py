"""
Consider a database table, Emails, which has the attributes
First Name and Email ID. Given N rows of data simulating the
Emails table, print an alphabetically-ordered list of people
whose email address ends in @gmail.com.

Input Format:
The first line contains an integer, N, total number of rows
in the table. Each of the N subsequent lines contains 2
space-separated strings denoting a person's first name and
email ID, respectively.
"""

# This problem does not actually require regex in python.


N = 6
list = ['riya riya@gmail.com', 'julia julia@julia.me',
		'julia sjulia@gmail.com', 'julia julia@gmail.com',
		'samantha samantha@gmail.com', 'tanya tanya@gmail.com']

outList = []

# N = int(input().strip())
for i in range(N):
	# firstName, emailID = input().strip().split(' ')
	firstName, emailID = list[i].strip().split(' ')
	# firstName, emailID = [str(firstName), str(emailID)]
	if "@gmail.com" in emailID:
		outList.append(firstName)


outList.sort()
for i in outList:
	print(i)

