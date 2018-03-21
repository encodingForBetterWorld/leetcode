# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    ret = 0
    min_p = None
    min_idx = 0
    max_p = 0
    max_idx = 0
    for idx, price in enumerate(prices):
        if min_p is None:
            min_p = price
            min_idx = idx
        elif min_p >= price:
            min_p = price
            min_idx = idx
        if max_p <= price:
            max_p = price
            max_idx = idx
        if min_idx < max_idx:
            ret = max(ret, max_p-min_p)
        elif min_idx == max_idx:
            pass
        else:
            max_idx = idx
            max_p = price
    return ret

print maxProfit([7, 1, 5, 3, 6, 4])