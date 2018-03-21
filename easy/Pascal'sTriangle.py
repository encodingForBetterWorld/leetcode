# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ret = []
    pre = None
    while numRows:
        tmp = []
        if isinstance(pre, list):
            pre_n = None
            for item in pre:
                if isinstance(pre_n, int):
                    tmp.append(item + pre_n)
                else:
                    tmp.append(item)
                pre_n = item
        numRows -= 1
        tmp.append(1)
        pre = tmp
        ret.append(tmp)
    return ret

ret = generate(10)
mid = len(ret)
for level in generate(10):
    print " " * mid, " ".join([str(n) for n in level])
    mid -= 1