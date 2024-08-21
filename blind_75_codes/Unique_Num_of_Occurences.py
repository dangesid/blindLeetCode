# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

dict = {}
arr = [-3,0,1,-3,1,1,1,-3,10,0]
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] = 1
print(dict)
arr_2 = []
for k, v in enumerate(dict):
    print(dict[v])
    arr_2.append(dict[v])
print(arr_2)


if len(arr_2) == len(set(arr_2)):
    print("True")
else:
    print("False ")