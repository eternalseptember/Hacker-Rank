"""
Input Format:
The first line contains a single string, a.
The second line contains a single string, b.

Output Format:
Print a single integer denoting the number of characters
you must delete to make the two strings anagrams of each other.
"""


def number_needed(a, b):
    copy_a = list(a)
    copy_b = list(b)
    unmatched = 0
    for letter in copy_a:
        try:
            copy_b.remove(letter)
        except:
            unmatched += 1

    remaining = len(copy_b)
    return unmatched + remaining


a = input().strip()
b = input().strip()

print(number_needed(a, b))

