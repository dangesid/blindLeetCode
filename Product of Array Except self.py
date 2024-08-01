# Given an integer array nums return an array answer such that answer[i] is equal to the product of all the
# elements of nums except nums[i]

# Input: nums[i] = [1,2,3,4]

# Output: answer[i] =  [24,12,8,6]


# Solution Approach : Basically Multiply all the elements and save that number and divide by arr[i] from range 0,
# len(arr) product --> 24 solution : [24/1, 24/2, 24/3, 24/4] Output array But it will not work when the input array
# has 0 as it will give the division0 error therefore we are not allowed to use Division operator.

# Second Approach: Maintain 2 arrays with left and right and omit the nums[i] : for example answer[0]:{arr_1 = [],arr_2 =[2,3,4]}
# answer[0] = multiply all the elements of arr2 and arr1 and append it to answer as a 0th element

def product(nums):
    n  = len(nums)
    result = [1] * n

    left_products = [1]*n
    right_products = [1] * n

    for i in range(1,n):
        left_products[i] = left_products[i-1] * nums[i-1]

    for i in range(n-2,-1,-1):
        right_products[i] = right_products[i+1]* nums[i+1]

    for i in range(n):
        result[i] = left_products[i] * right_products[i]
    return result

nums = [-1,1,0,-3,3]
print(product(nums))