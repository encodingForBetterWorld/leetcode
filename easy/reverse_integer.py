
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    is_lz = x<0
    if is_lz:
        x *= -1
    arr = []
    rtype = 0
    level = 1
    while x:
        arr.append(x%10)
        x/=10
        level *= 10
    for num in arr:
        rtype += num * level/10
        if rtype < -(2**31) or rtype > (2**31 - 1):
            return 0
        level /= 10
    if is_lz:
        rtype*=-1
    return rtype

print reverse(-2149)