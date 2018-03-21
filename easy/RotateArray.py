# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
#
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II

def reverse(nums, s, e):
    while s <= e:
        tmp = nums[s]
        nums[s] = nums[e]
        nums[e] = tmp
        s += 1
        e -= 1

def rotate2right(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    k %= l
    reverse(nums, 0, l-1)
    reverse(nums, k, l-1)
    reverse(nums, 0, k - 1)

def rotate2left(nums, k):
    rotate2right(nums, len(nums)-k)


nums = [1,2,3,4,5,6,7]

rotate2right(nums, 5)
print nums