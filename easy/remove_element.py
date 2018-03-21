def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    max = len(nums)
    count = 0
    idx = 0
    while idx < max:
        if val == nums[count]:
            del nums[count]
        else:
            count += 1
        idx += 1
    return count

print removeElement([2,3,3,3,2], 3)