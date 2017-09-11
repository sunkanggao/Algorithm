# -*- coding:utf-8 -*-

import numpy as np


def LCS(str1, str2):
    """
    动态规划求解
    最长公共子序列
    Xi是字符串X的i前缀
    Yj是字符串Y的j前缀
    chess[i, j]记录序列Xi和Yj的最长公共子序列长度。
    1. xm = yn时，LCS(Xm, Yn) = LCS(Xm-1, Yn-1) + 1
    2. xm != yn时，LCS(Xm, Yn) = max(LCS(Xm-1, Yn), LCS(Xm, Yn-1))
    计算c[][]矩阵的时间复杂度是O(m*n)；
    根据b[][]矩阵寻找最长公共子序列的过程，由于每次调用至少向上或向左移动一步，这样最多需要（m+n）次就会i = 0或j = 0，
    也就是算法时间复杂度为O(m+n)。
    :param str1: 字符串1
    :param str2: 字符串2
    :return: 字符串1和字符串2的最长公共子序列
    """
    size1 = len(str1)
    size2 = len(str2)
    chess = np.zeros((size1 + 1, size2 + 1))
    for i in range(1, size1 + 1):
        for j in range(1, size2 + 1):
            if str1[i - 1] == str2[j - 1]:
                chess[i, j] = chess[i - 1, j - 1] + 1
            else:
                chess[i, j] = max(chess[i - 1, j], chess[i, j - 1])
    # 回溯
    s = list()
    i = size1
    j = size2
    while i != 0 and j != 0:
        if str1[i - 1] == str2[j - 1]:
            s.append(str1[i - 1])
            i -= 1
            j -= 1
        else:
            if chess[i, j - 1] > chess[i - 1, j]:
                j -= 1
            else:
                i -= 1
    s.reverse()
    return ''.join(s)


if __name__ == '__main__':
    str1 = 'ABCBDAB'
    str2 = 'BDCABA'
    print str1
    print str2
    print u'最长公共子序列为', LCS(str1, str2)
