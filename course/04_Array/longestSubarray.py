# -*- coding:utf-8 -*-

"""
给定长度为N的数组A[0...N-1]，求递增且连续数字最长的子数组。
"""


def longestSubarray(array):
    size = len(array)
    if size == 1:
        return 1
    m = 1
    cur = 1
    for i in range(1, size):
        if array[i] - array[i - 1] == 1:
            cur += 1
        else:
            m = max(cur, m)
            cur = 1
    return m


if __name__ == '__main__':
    array = [1, 2, 3, 34, 56, 57, 58, 59, 60, 61, 99, 121]
    print longestSubarray(array)

