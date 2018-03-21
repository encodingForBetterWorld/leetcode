# coding=utf-8
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
import math
# def majorityElement(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     ret = None
#     if len(nums) == 0:
#         return ret
#     d = {}
#     le = math.ceil(len(nums)/2.0 + 0.1)
#     for num in nums:
#         count = d.get(num, 0) + 1
#         if count >= le:
#             return num
#         else:
#             d[num] = count

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 1
    major = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == major:
            count += 1
        else:
            count -= 1
            if count == 0:
                count = 1
                major = nums[i]
    return major

print majorityElement([6,7,6,7,6,7,6])