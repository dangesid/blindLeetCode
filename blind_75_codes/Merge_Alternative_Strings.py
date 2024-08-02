# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

str_1 = ""
lst = []

word_1 = "abc"
word_2 = "pqr"
max_len = max(len(word_1),len(word_2))
# print(max_len)

for i in range(max_len):
    # print(i)
    if i < len(word_1):
        lst.append(word_1[i])
    if i < len(word_2):
        lst.append(word_2[i])
merged_str = "".join(lst)
print(merged_str)