# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# The number of elements initialized in nums1 and nums2 are m and n respectively.

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    idx = 0
    le = m + n
    tmp = []
    nums2 = nums2[:n]
    while len(nums1) - m:
        nums1.pop()
    while idx < le:
        n1 = n2 = nt = None
        if idx < m:
            n1 = nums1[idx]
        if nums2:
            n2 = nums2[0]
        if tmp:
            nt = tmp[0]
        if n1 is None:
            if n2 is None:
                nums1.extend(tmp)
                break
            elif nt is None:
                nums1.extend(nums2)
                break
            else:
                if n2 < nt:
                    nums1.append(n2)
                    nums2.pop(0)
                else:
                    nums1.append(nt)
                    tmp.pop(0)
                m += 1
        elif n2 is None:
            if nt is None:
                break
            else:
                if nt < n1:
                    tmp.pop(0)
                    tmp.append(n1)
                    if idx < m:
                        nums1[idx] = nt
                    else:
                        nums1.append(nt)
                        m += 1
        else:
            if n1 > n2:
                if nt is not None and n2 > nt:
                    if idx < m:
                        nums1[idx] = nt
                    else:
                        nums1.append(nt)
                        m += 1
                    tmp.pop(0)
                else:
                    if idx < m:
                        nums1[idx] = n2
                    else:
                        nums1.append(n2)
                        m += 1
                    nums2.pop(0)
                tmp.append(n1)
            else:
                if nt is not None and n1 > nt:
                    if idx < m:
                        nums1[idx] = nt
                    else:
                        nums1.append(nt)
                    tmp.pop(0)
                    tmp.append(n1)
        idx += 1


nums1 = [-1,0,1,1]
nums2 = [-1,0,2,2,3]
merge(nums1, 4, nums2, 5)
print nums1