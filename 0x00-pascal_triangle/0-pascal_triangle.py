#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        tri_list = []
        for i in range(n):
            if i == 0:
                tri_list.append([1])
            else:
                new_list = [1]
                prev = tri_list[i - 1]
                for j in range(len(prev) - 1):
                    sum = prev[j] + prev[j + 1]
                    new_list.append(sum)

                new_list.append(1)
                tri_list.append(new_list)
        return tri_list
