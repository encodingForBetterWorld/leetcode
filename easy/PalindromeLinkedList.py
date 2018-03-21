# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?

from leetcode.common import ListNode

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    pre = None
    tmp = None
    c = 0
    while fast and slow:
        fast = fast.next
        c += 1
        if fast:
            fast = fast.next
            c += 1
        tmp = slow
        slow = slow.next
        tmp.next = pre
        pre = tmp
    if c % 2 == 1:
        tmp = tmp.next
    while slow and tmp:
        if tmp.val != slow.val:
            return False
        tmp = tmp.next
        slow = slow.next
    return True

head = ListNode.arrayToTreeNode([1,5,4,3,4,5,1])
print isPalindrome(head)
