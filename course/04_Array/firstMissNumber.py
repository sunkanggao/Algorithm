# -*- coding:utf-8 -*-

"""
给定一个数组A[0 ... N-1]，找到从1开始，第一个不在数组中的正整数。
循环不变式：如果某命题初始为真，且每次更改后仍然保持该命题为真，
则若干次更改后该命题仍为真。
"""

def firstMissNumber(a):
    """
    找到输入数组中第一个不在数组中的正整数。
    方法：假定前i-1个数已经找到，并依次存放在a[1,2,...,i-1]中，继续考察a[i]。
    如何快速丢弃A[i]？将A[size]赋值给A[i]，然后size减1。
    :param a:
    :return:
    """
    size = len(a)
    a.insert(0, 0)    # 为方便，从1开始数
    i = 1
    while i <= size:
        if a[i] == i:
            i += 1
        elif a[i] < i or a[i] > size or a[a[i]] == a[i]:    # 丢弃A[i]
            a[i] = a[size]
            size -= 1
        else:    # a[i] > i
            tmp = a[i]
            a[i], a[tmp] = a[tmp], a[i]
    return i


if __name__ == '__main__':
    a = [3, 5, 1, 2, -3, 7, 14, 8]
    print firstMissNumber(a)



