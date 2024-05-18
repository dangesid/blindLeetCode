# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

arr = [2,7,11,15]
target = 9
n = len(arr)

for i in range(0,len(arr)):
    for j in range(0,n-1):
        if arr[i] + arr[j] == target:
            print(i,j)
        break
print("Hii this question is solved ")