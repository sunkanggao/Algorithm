# -*- coding:utf-8 -*-
"""
用manacher算法解决最长回文子串问题
"""


def manacher(s):
    """
    :param s:
    :return: 数组p，用一个数组p[i]来记录以字符S[i]为中心的最长回文子串
    向左/右扩展的长度（包括s[i]）。则最长回文子串为最大的p[i]-1。
    """
    # 讲原串转化为Gap串
    s = '#' + '#'.join(s) + '#'
    size = len(s)
    p = [0] * size
    p[0] = 1
    id = 0
    mx = 1
    for i in range(1, size):
        if mx > i:
            p[i] = min(p[2*id - i], mx - i)
        else:
            p[i] = 1

        while i + p[i] < size and s[i + p[i]] == s[i - p[i]]:
            p[i] += 1

        if mx < i + p[i]:
            mx = i + p[i]
            id = i
    return max(p) - 1


if __name__ == '__main__':
    s = '12212321'
    print manacher(s)