# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    one = 0
    accumulation = 0
    for num in nums:
        accumulation |= num & one
        one ^= num
        t = one & accumulation
        one &= ~t
        accumulation &= ~t
    return one
