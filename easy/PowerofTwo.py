# Given an integer, write a function to determine if it is a power of two.
def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n:
        if n > 1 and n % 2 == 1:
            return False
        n /= 2
    return True