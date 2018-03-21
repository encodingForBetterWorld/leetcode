# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    d1 = {}
    d2 = {}
    count = 0
    while count < len(s):
        ch1 = s[count]
        ch2 = t[count]
        if d1.has_key(ch1) and d1.get(ch1) != ch2:
            return False
        if d2.has_key(ch2) and d2.get(ch2) != ch1:
            return False
        d1[ch1] = ch2
        d2[ch2] = ch1
        count += 1
    return True

print isIsomorphic("eggeg","addad")