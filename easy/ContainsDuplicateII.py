# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    t = {}
    if not nums or len(nums) < 2:
        return False
    ret = False
    for idx, num in enumerate(nums):
        if t.has_key(num) and idx - t[num] <= k:
            return True
        t[num] = idx
    return ret


print containsNearbyDuplicate([5,2,3,4,5],6)