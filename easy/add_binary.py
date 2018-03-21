# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100"
import requests
def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    al = len(a)
    bl = len(b)
    ret = ""
    is_plus = False
    while al or bl:
        n1 = n2 = 0
        if al:
            n1 = int(a[al-1])
            al -= 1
        if bl:
            n2 = int(b[bl-1])
            bl -= 1
        n = n1 + n2 + (is_plus and 1 or 0)
        if n < 2:
            is_plus = False
        else:
            n -= 2
            is_plus = True
        ret = str(n) + ret
    if is_plus:
        ret = "1" + ret
    return ret

print addBinary("11", "11")