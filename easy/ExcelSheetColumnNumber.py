# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    ret = 0
    le = len(s)
    c = 1
    while le:
        le -= 1
        ch = s[le]
        ret += ((ord(ch) - 65 + 1) * c)
        c *= 26
    return ret

print titleToNumber('AAA')
