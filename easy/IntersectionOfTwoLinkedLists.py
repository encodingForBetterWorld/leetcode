# coding=utf-8
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: L
    """
    tail_a = headA
    tail_b = headB
    short = None
    longer = None
    diff = None
    if headA == headB:
        return headA
    while tail_a and tail_b:
        if tail_a.next == tail_b.next:
            if tail_a.next is None:
                return None
            else:
                return tail_a.next
        else:
            if tail_a.next is None:
                diff = tail_b.next
                short = headA
                longer = headB
                break
            elif tail_b.next is None:
                diff = tail_a.next
                short = headB
                longer = headA
                break
        tail_a = tail_a.next
        tail_b = tail_b.next
    while diff:
        longer = longer.next
        diff = diff.next
    while short and longer:
        if short == longer:
            return short
        short = short.next
        longer = longer.next
    return None

from leetcode.common.ListNode import ListNode
n = ListNode(1)
print getIntersectionNode(n, n)