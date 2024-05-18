# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[i] + arr[j] == target:
                print(i,j)
        break

if __name__ =="__main__":
    arr = [2,7,11,15]
    target = 9
    two_sum(arr)