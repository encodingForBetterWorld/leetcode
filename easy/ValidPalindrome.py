# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True
    count = 0
    le = len(s) - 1
    for idx, ch in enumerate(s):
        if ch.isalpha() or ch.isalnum():
            rch = None
            rle = le - count
            while rle >= idx:
                rch = s[rle]
                if rch.isalpha() or rch.isalnum():
                    break
                else:
                    rle -= 1
                    count += 1
            rle = le - count
            if rle == idx:
                return True
            if ch.lower() != rch.lower():
                return False
            if rle == idx + 1:
                return True
            count += 1
        else:
            if le - count == idx:
                return True
    return True

print isPalindrome("abba")