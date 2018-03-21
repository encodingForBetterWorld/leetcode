# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    ret = 0
    for idx, price in enumerate(prices):
        if idx:
            pre_price = prices[idx - 1]
            if price > pre_price:
                ret += price - pre_price
    return ret
print maxProfit([7,1, 5, 3, 6, 4,8])