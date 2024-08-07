arr = [1,2,3,4,5]
lst = []

if len(arr)<3:
    print("False")
else:
    min1 = float('inf')
    min2 = float('inf')
    found = False

    for i in arr:
        if i <= min1:
            min1 = i
        elif i <= min2:
            min2 = i
        else:
            found = True
            break

    if found:
        print(True)
    else:
        print(False)
