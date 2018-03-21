# coding=utf-8
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.

# 假设走完k个台阶有f(k)种走法。
# k = 1时，f(k) = 1
# k = 2时，f(k) = 2
# k = n时，第一步走一个台阶，剩n-1个台阶，有f(n - 1)种走法。
# 第一步走两个台阶，剩n-2个台阶，有f(n - 2)种走法。所以共有f(n - 1) + f(n - 2)种走法。
# 于是有函数
# f(1) = 1
# f(2) = 2
# f(n) = f(n-1) + f(n-2)

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    a, b = 0, 1
    while n+1:
        a, b = a + b, a
        n -= 1
    return a

print climbStairs(10)

# 最多可以走三步呢？
# f(1) = 1
# f(2) = 2
# f(3) = 4
# f(n) = f(n-1) + f(n-2) + f(n-3)

def climbStairs(n):
    """
    :param n:
    :return:
    """
    a, b, c = 0, 0, 1
    while n + 1:
        a, b, c = a + b + c, a, b
        n -= 1
    return a

print climbStairs(10)