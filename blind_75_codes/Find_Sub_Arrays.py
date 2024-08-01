def print_all_subarrays(nums):
    sub_arr = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarr = nums[i:j + 1]
            sub_arr.append(subarr)
    for subarr in sub_arr:
        print(subarr)

nums = [5, 4, -1, 7, 8]
print_all_subarrays(nums)
