# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    count = 0
    idx = 0
    le = len(needle)
    if le == 0:
        return 0
    while idx < len(haystack):
        ch = haystack[idx]
        ch1 = needle[count]
        if ch == ch1:
            count += 1
        else:
            idx -= count
            count = 0
        if count == le:
            return idx - count + 1
        idx += 1
    return -1

print strStr("mississippi", "pi")