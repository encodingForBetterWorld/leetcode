# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # for idx, num in enumerate(nums):
    #     for i, n in enumerate(nums[idx+1:]):
    #         if n + num == target:
    #             return [idx, idx+1+i]
    pairs = {}
    for idx, val in enumerate(nums):
        if val in pairs:
            return [pairs[val], idx]
        else:
            pairs[target - val] = idx
print twoSum([2, 7, 11, 15], 9)