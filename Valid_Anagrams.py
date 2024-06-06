# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
"""
t = "nagaram"
s = "anagram"


def count_char(string):
    count = {}
    for i in string:
        if i in count:
            count[i] +=1
        else:
            count[i] = 0
    return count
if len(s) != len(t):
    print("False")

count_s = count_char(s)
count_t = count_char(t)

if count_s == count_t:
    print("true")
else:
    print("False")


def count_char(string):
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
"""

def count_char(string):
    count = {}
    for i in string:
        if i in count:
            count[i] +=1
        else:
            count[i] = 0
    return count

def are_anagrams(s: str, t: str) -> bool:
    # Check if lengths of strings are equal
    if len(s) != len(t):
        return False

    # Count characters in both strings
    count_s = count_char(s)
    count_t = count_char(t)

    # Check if the two dictionaries are equal
    return count_s == count_t


# Test the function
t = "nagaram"
s = "anagram"
print(are_anagrams(s, t))