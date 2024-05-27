# Input: a[] = {-5, 3, 6, 12, 15}, b[] = {-12, -10, -6, -3, 4, 10}
# Output: The median is 3.

# Explanation : The merged array is: ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20}
# If the number of the elements are even. So there are two middle elements.
# Take the average between the two: (10 + 12) / 2 = 11.

a = [2,3,5,8]
b = [10, 12, 14, 16, 18, 20]
a3 = lambda a,b: a+b
a3 = a3(a,b)
print(len(a3))

for i in range(0,len(a3)):
    for j in range(0,len(a3)-i-1):
        if a3[j]>a3[j+1]:
            a3[j],a3[j+1]=a3[j+1],a3[j]


for i in range(0,len(a3)):
    print(a3[i],end = " ")

median = 0
if len(a3) % 2 != 0:
    median_index = len(a3) // 2  # Get the middle index for odd length
    median = a3[median_index]
else:
    median_index1 = len(a3) // 2  # Lower middle index for even length
    median_index2 = median_index1 - 1  # Upper middle index
    median = (a3[median_index1] + a3[median_index2]) / 2
print("\n")
print("Median:", median)