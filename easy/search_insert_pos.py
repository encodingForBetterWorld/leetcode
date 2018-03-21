# coding=utf-8
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
import math
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    le = len(nums)
    mid = (le-1)/2
    step = 0
    high = count = le
    while count:
        if le < mid:
            break
        mid += step
        num = nums[mid]
        if num < target:
            step = (high - mid)/2
        elif num > target:
            high = mid
            step = -mid/2
        else:
            return mid
        count -= 1
    if nums[mid] < target:
        return mid + 1
    else:
        return mid

print searchInsert([1,3,5], 0)