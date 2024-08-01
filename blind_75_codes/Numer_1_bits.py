# Write a function that takes the binary representation of a positive integer and returns the number of
# set bits it has (also known as the Hamming weight).

# Input: n = 11
#
# Output: 3
#
# Explanation:
#
# The input binary string 1011 has a total of three set bits.
n = 128
count = 0

while n>0:
    if n&1:
        count+=1
    n>>=1
print(count)



