#!/usr/bin/python3
""" Module to Rotate a 2D Matrix """


def rotate_2d_matrix(matrix):
    """ rotates an n x n 2d matrix by 90 """
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            top_left = matrix[top][l + i]

            matrix[top][l + i] = matrix[bottom - i][l]

            matrix[bottom - i][l] = matrix[bottom][r - i]

            matrix[bottom][r - i] = matrix[top + i][r]

            matrix[top + i][r] = top_left

        r -= 1
        l += 1
