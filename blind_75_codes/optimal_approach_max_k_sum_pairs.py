seen = {}
pairs = []
result = []
arr = [1,2,3,4]
k = 5
for i in arr:
    target = k - i
    if target in seen and seen[target] > 0:
        pairs.append((target,i))
        seen[target]-=1
    else:
        if i in seen:
            seen[i]+=1
        else:
            seen[i] = 1
        result.append(i)
print(result,pairs)
print(len(pairs))