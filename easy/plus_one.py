# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
from collections import deque
import requests
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    ret = deque()
    idx = len(digits)
    is_plus = False
    is_first = True
    while idx:
        num = digits[idx - 1]
        if is_first:
            is_first = False
            num += 1
        if is_plus:
            num += 1
        if num < 10:
            is_plus = False
        else:
            is_plus = True
            num %= 10
        ret.appendleft(num)
        idx -= 1
    if is_plus:
        ret.appendleft(1)
    return list(ret)

print plusOne([9,9])