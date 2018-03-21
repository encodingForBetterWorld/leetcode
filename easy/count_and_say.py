# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    ret = "1"
    pre_str = None
    for i in range(0,n):
        li = ""
        if pre_str:
            pr = None
            c = 0
            for p in pre_str:
                if pr is None:
                    pr = p
                if pr is not None and pr != p:
                    li+="%s%s" % (c, pr)
                    c = 0
                pr = p
                c += 1
            li += "%s%s" % (c, pr)
            pre_str = li
        else:
            li += "1"
            pre_str = li
        ret = li
    return ret

print countAndSay(6)