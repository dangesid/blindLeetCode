# Given a string s, find the length of the longest
# substring without repeating characters.
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 3:
#
# Input: s = "bbbbb"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


charset = set()
s = "abcabcbb"
l=0

res = 0
for r in range(0,len(s)):
    while s[r] in charset:
        charset.remove(s[l])
        l+=1
    charset.add((s[r]))
    res = max(res,r-l+1)
print(res)
