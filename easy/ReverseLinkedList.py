from leetcode.common.ListNode import ListNode
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    pre = None
    ret = None
    while head:
        tmp = head
        head = head.next
        ret = tmp
        ret.next = pre
        pre = tmp
    return ret

h = ListNode(1)
h.next = ListNode(2)
h = reverseList(h)
print h