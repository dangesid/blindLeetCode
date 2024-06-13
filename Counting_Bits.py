# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number
# of 1's in the binary representation of i.
#

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

n = 2
setbits = []
for i in range(0, n+1):
    ans = bin(i).replace("0b", "")
    setbits.append(ans)
print(setbits)

counts = [bits.count("1") for bits in setbits]
print(counts)

