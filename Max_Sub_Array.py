# Given an integer array nums, find the #subarray
#  with the largest sum, and return its sum.

# Example 1:
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Naive or Beginner approach --> time complexity n cube (n^3)
# find the sum of all the sub array and return the subarray with max sum

def max_subarray_sum(nums):
    if not nums:
        return 0, []

    max_sum = float("-inf")
    max_subarray = []

    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            curr_sum = 0
            sub_arr = []
            for k in range(i,j+1):
                curr_sum += nums[k]
                sub_arr.append(nums[k])
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_subarray = sub_arr
    return max_sum, max_subarray

nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum , max_subarray = max_subarray_sum(nums)
print(max_sum)
print(max_subarray)