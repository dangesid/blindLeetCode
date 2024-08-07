# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.

# Example 1:
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

string = "aaa"

res = 0
for i in range(len(string)):
    r = l = i
    while l>= 0 and r<len(string) and string[l] == string[r]:
        res+=1
        l-=1
        r+=1

    l = i
    r = i+1

    while l>=0 and r<len(string) and string[l] == string[r]:
        res+=1
        l-=1
        r+=1
print(res)



