# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without
# disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
#
# Input: s = "abc", t = "ahbgdc"

# Output: true


s = "abc"
t = "ahbgdc"

# Two Pointer Approach

# i = 0
# j = 0
# while i<len(s) and j < len(t):
#     if s[i] == t[j]:
#         i+=1
#     j+=1
# if i == len(s):
#     print(True)
# else:
#     print(False)
p1 = 0
string_2 = ""
n1 = len(s)
n2 = len(t)

for i in range(n1):
    for j in range(p1,n2):
        if s[i] == t[j]:
            string_2 += s[i]
            p1 = j+1
            break
print(string_2)
if s == string_2:
    print(True)
else:
    print("False")