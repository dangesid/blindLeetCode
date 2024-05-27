# bubble Sort

arr = [2,23,10,1]

for i in range(0,len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

for i in range(0,len(arr)):
    print(arr[i],end=",")