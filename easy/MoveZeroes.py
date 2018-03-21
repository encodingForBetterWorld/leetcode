# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
#
#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

def moveZeroes(nums):
    i = 0
    j = 0
    while i < len(nums):
        n1 = nums[i]
        if n1 == 0:
            i += 1
            while i < len(nums):
               n2 = nums[i]
               if n2:
                   nums[i] = nums[j]
                   nums[j] = n2
                   j += 1
                   break
               i += 1
        else:
            i += 1
            j += 1


test = [20, 0, 0, 1, 0, 3, 0, 1, 22]
moveZeroes(test)
print test