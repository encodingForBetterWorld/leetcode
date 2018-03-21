def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = None
    for num in nums:
        if ret is None:
            ret = num
        else:
            ret ^= num
    return ret
print singleNumber([2,3,3,2,5])