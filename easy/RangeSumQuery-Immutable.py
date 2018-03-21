# coding=utf-8
# Given an integer array nums,
# find the sum of the elements between indices i and j (i ≤ j), inclusive.

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0] * (len(nums) + 1)
        for i in xrange(1, len(nums) + 1):
            self.sums[i] = self.sums[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]

ns = NumArray([-2, 0, 3, -5, 2, -1])
print ns.sumRange(0,2)
print ns.sumRange(2,5)
print ns.sumRange(0,5)