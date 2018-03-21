# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    pre_max_pro = 0
    next_max_pro = 0
    ret = 0
    if len(prices) < 2:
        return 0
    le = len(prices)
    pre_min = prices[0]
    next_max = prices[-1]
    pro_dict = {}
    for idx, price1 in enumerate(prices):
        next_idx = le - idx - 1
        if price1 < pre_min:
            pre_min = price1
        price2 = prices[next_idx]
        if price2 > next_max:
            next_max = price2
        pre_max_pro = max(pre_max_pro, price1 - pre_min)
        next_max_pro = max(next_max_pro, next_max - price2)
        if next_idx < idx:
            pro1 = pro_dict.get(idx)
            ret = max(ret, pre_max_pro + pro1)
            pro2 = pro_dict.get(next_idx)
            ret = max(ret, next_max_pro + pro2)
        else:
            pro_dict[idx] = pre_max_pro
            pro_dict[next_idx] =  next_max_pro
    return ret

print maxProfit([3,3,5,0,0,3,1,4])
