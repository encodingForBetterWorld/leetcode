"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    idx = 0
    while idx < len(nums):
        i = idx+1
        if idx == len(nums) -1:
            idx += 1
            break
        num = nums[idx]
        if nums[i] != num:
            idx += 1
        else:
            del nums[i]
    # print nums
    return idx
print removeDuplicates([1,1,2])