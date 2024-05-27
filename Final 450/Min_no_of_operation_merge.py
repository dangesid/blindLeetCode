#Input : arr[] = {1, 4, 5, 1}
# Output : 1
# We can make given array palindrome with
# minimum one merging (merging 4 and 5 to
# make 9)

# 2 pointer approach
# if the elements from 2 pointers are not equal just merge it
merge = 0
arr = [1,4,5,1]
i = 0
j = len(arr)-1

while i<=j:
    if arr[i] == arr[j]:
        i+=1
        j-=1

    elif arr[i]>arr[j]:
        j-=1
        arr[j] += arr[j+1]
        merge += 1
    else:
        i+=1
        arr[i] += arr[i-1]
        merge+=1
print(merge)