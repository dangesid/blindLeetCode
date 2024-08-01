# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
# Example 1:
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range
# since it does not appear in nums.

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# sum of first n natural number - sum of the numbers in the arr

num = len(nums)
print(int(num * (num + 1) / 2))
sum_1 = int(num * (num + 1) / 2)

sum_2 = sum(nums)
print(sum_2)

missing_num = sum_1 - sum_2
print(missing_num)

# ------------------------ LEETCODE OOPS WAY -----------------------------

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        sum_1 = int(num * (num + 1) / 2)
        sum_2 = sum(nums)
        return sum_1 - sum_2


solution = Solution()
nums = [3, 0, 1]
missing = solution.missingNumber(nums)
print(missing)
