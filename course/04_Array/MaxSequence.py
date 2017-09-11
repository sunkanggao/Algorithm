# -*- coding:utf-8 -*-

def maxSequence(array):
    size = len(array)
    p = [1] * size
    m = 1
    for i in range(1, size):
        if array[i] - array[i - 1] == 1:
            p[i] += p[i - 1]
            m = max(m, p[i])
    return m


if __name__ == '__main__':
    array = [1, 2, 3]