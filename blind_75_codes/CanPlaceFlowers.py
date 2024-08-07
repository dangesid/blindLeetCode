arr = [1,0,0,0,1]
n = 1

if n == 0:
    print(False)
else:
    for i in range(len(arr)):
        if arr[i] == 0 and (i==0 or arr[i-1] == 0) and( i == len(arr)-1 or arr[i+1] == 0):
            arr[i] = 1
            n -= 1
            if n == 0:
                print(True)
                break
    if n > 0:
        print(False)

