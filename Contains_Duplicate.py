# given an array nums if any value appears atleast twice return true else false
# nums = [1,2,3,1]
# TRUE

arr = [1,1,2,3,4,5,5,5,6,7,7,7,8,8,9,10]

# duplicate_found = False
# for i in range(len(arr)):
#     for j in range(i):
#         if arr[i] == arr[j]:
#             print("true")
#             duplicate_found = True
#             break
#     if duplicate_found:
#         break
#     else:
#         print("False")
#

seen = set()
duplicates = set()
def duplicates(arr):
    for i in arr:
        if i in seen:
            return True

        else:
            seen.add(i)
    return False

