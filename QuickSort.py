def partition(a,start,end):
    i = (start - 1)
    pivot = a[end]

    for j in range(start,end):
        if (a[j]<=pivot):
            i +=1
            a[i],a[j] = a[j],a[i]

    a[i+1],a[end] = a[end],a[i+1]
    return (i+1)

def quick_sort(a,start,end):
    if (start<end):
        p = partition(a,start,end)
        quick_sort(a,start,p-1)
        quick_sort(a,p+1,end)

def printArr(a):
    for i in range(len(a)):
        print(a[i],end = ",")

a = [68,13,1,49,58]
quick_sort(a,0,len(a)-1)
printArr(a)