# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#iterate through each item and compare every element if its negative leave it and positive
#then compare all positive and return the min

# arr[i] = price of stock
# i = day
# #
# list_1 = []
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         res = arr[j]-arr[i]
#         list_1.append(res)
# print(list_1)
# print(max(list_1))

prices = [7,1,5,3,6,4]

## Better Approach

buy = prices[0]
profit = 0

for sell in prices:
    profit = max(profit, sell - buy)

    if sell < buy:
        buy = sell
print( profit)