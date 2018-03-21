# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

from functools import reduce
from collections import deque

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    ret = [1]
    if rowIndex == 1:
        ret.append(1)
    elif rowIndex > 1:
        ret.append(rowIndex)
        for row in range(2, rowIndex):
            ret.append(ret[row - 1] * (rowIndex - (row - 1)) / row)
        ret.append(1)
    return ret
print getRow(1)