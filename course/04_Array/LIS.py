# -*- coding:utf-8 -*-

"""
给定一个数组，求该数组的最长递增子序列。
方法一：先对该数组排序（NlogN），求原数组与排序数组的LCS（N^2）。
"""

def LIS(array, pre):
    """
    以a[i]结尾的最长递增子序列记为Li，其长度记为b[i]。
    动态规划：b[i] = {max(b[j] + 1, 0<=j<i 且 a_j<=a_i}
    :param array: 原数组
    :param pre: 记录以a[i]结尾的最长递增子序列的前一个元素的索引
    :return: 最长递增子序列的长度，以及其最后一个元素的索引
    """
    size = len(array)
    b = [1] * size
    curMax = 1
    idx = 0
    for i in range(1, size):
        for j in range(0, i):
            if array[j] <= array[i]:
                if b[i] < b[j] + 1:
                    b[i] = b[j] + 1
                    pre[i] = j
        if b[i] > curMax:
            curMax = b[i]
            idx = i
    return curMax, idx

def getLIS(array, pre, mId):
    """
    获取最长递增子序列
    :param array: 原数组
    :param pre: 以a[i]结尾的最长递增子序列的前一个元素索引的数组
    :param mId: 最长递增子序列最后一个元素的索引
    :return: 最长递增子序列
    """
    lis = []
    while mId >= 0:
        lis.append(array[mId])
        mId = pre[mId]
    lis.reverse()
    return lis


if __name__ == '__main__':
    array = [1, 4, 6, 2, 8, 9, 7]
    pre = [-1] * len(array)    # 记录以a[i]结尾的最长递增子序列的前一个元素的索引
    mLen, mId = LIS(array, pre)
    print u'原数组\n', array
    print u'最长递增子序列长度\n', mLen
    print u'最长递增子序列\n', getLIS(array, pre, mId)

