# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    p_max = None
    c_max = None
    for num in nums:
        if c_max is None:
            p_max = c_max = num
        else:
            if c_max < 0:
                c_max = num
                if c_max > p_max:
                    p_max = num
            else:
                c_max += num
                p_max = max(p_max, c_max)
    return max(p_max, c_max)
print maxSubArray([1,-2,0])
