# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    queen = []
    b, e = 0, len(s) - 1
    s = list(s)
    while b <= e:
        ch1, ch2 = s[b], s[e]
        if ch1.lower() in vowels and b < e:
            queen.append((b, ch1))
        if ch2.lower() in vowels:
            if len(queen) == 0:
                e += 1
            else:
                tmpi, tmpv = queen.pop(0)
                s[tmpi] = ch2
                s[e] = tmpv
        e -= 1
        b += 1
    b, e = 0, len(queen) - 1
    while b < e:
        bi, bv = queen[b]
        ei, ev = queen[e]
        s[bi] = ev
        s[ei] = bv
        b += 1
        e -= 1
    return ''.join(s)

print reverseVowels("Harass sensuousness, Sarah.")
