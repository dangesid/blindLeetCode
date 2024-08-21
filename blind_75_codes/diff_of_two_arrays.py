# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
#
#
#
# Example 1:
#
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]


nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

list_1 = [] # int present in num1 but not in num2 but distinct (unique)
list_2 = []
list_s = []
list_t = []
for i in nums1:
    if i not in nums2:
        list_1.append(i)
        list_s = set(list_1)
print(list(list_s))

for i in nums2:
    if i not in nums1:
        list_2.append(i)
        list_t = set(list_2)
print(list(list_t))

answer = list([list(list_s), list(list_t)])
print(answer)