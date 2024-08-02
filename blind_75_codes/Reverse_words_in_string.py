# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.

# Example 1:
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"

s = "the sky is blue  "

lst = []

z = s.split()
print(z)

for i in range(0,len(z)):
    ele = z.pop()
    lst.append(ele)

print(lst)

p = " ".join(lst)
print(p)