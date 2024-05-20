# given an array nums if any value appears atleast twice return true else false
# nums = [1,2,3,1]
# TRUE

arr = [1,1,1,3,3,4,3,2,4,2]

duplicate_found = False
for i in range(len(arr)):
    for j in range(i):
        if arr[i] == arr[j]:
            print("true")
            duplicate_found = True
            break
    if duplicate_found:
        break


