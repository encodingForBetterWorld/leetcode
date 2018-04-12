# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
#
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:
#
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    for i in range(int(len(matrix)/2)):
        for j in range(len(matrix)-(i*2)-1):
            s_idx = i + j
            c_idx = - i - j - 1
            tmp = matrix[s_idx][-i - 1]
            matrix[s_idx][-i - 1] = matrix[i][s_idx]
            tmp1 = matrix[-i - 1][c_idx]
            matrix[-i - 1][c_idx] = tmp
            tmp = matrix[c_idx][i]
            matrix[c_idx][i] = tmp1
            matrix[i][s_idx] = tmp

m =[[2,29,20,26,16,28],
    [12,27,9,25,13,21],
    [32,33,32,2,28,14],
    [13,14,32,27,22,26],
    [33,1,20,7,21,7],
    [4,24,1,6,32,34]]


rotate(m)
print m
