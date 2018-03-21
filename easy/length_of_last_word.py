# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    le = len(s)
    new_s = None
    low = len(s)
    p_tail = False
    while le:
        ch = s[le-1]
        if p_tail:
            if ch == " ":
                low -= 1
            else:
                p_tail = False
        else:
            if ch == " ":
                new_s = s[le: low]
                if new_s == "":
                    p_tail = True
                    low = le - 1
                else:
                    break
        le -= 1
    if new_s is None or new_s == "":
        new_s = s[le:low]
    return len(new_s)

print lengthOfLastWord("ab  ")