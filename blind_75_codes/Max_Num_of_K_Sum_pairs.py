# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.

arr = [1,2,3,4]
k = 5
count = 0
arr_2 = []

for i in range(len(arr)):
    if arr[i] is None:
        continue
    for j in range(i+1,len(arr)):
        if arr[j] is None:
            continue
        if arr[i] + arr[j] == k:
            print(arr[i],arr[j])
            arr_2.append((arr[i],arr[j]))
            count+=1
            arr[i] = None
            arr[j] = None
            break

arr = [x for x in arr if x is not None]
print(arr)
print(arr_2)
print(count)

# Time Limit Exceed with above Solution Not an Optimal approach


