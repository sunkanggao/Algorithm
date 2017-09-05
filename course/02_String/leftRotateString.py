# -*- coding:utf-8 -*-

"""
字符串循环左移
"""

def reverseString(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


def leftRotateString(s, n, m):
    """
    :param s: 字符串
    :param n: 字符串长度
    :param m: 循环左移位数
    :return:
    """
    m %= n
    reverseString(s, 0, m - 1)
    reverseString(s, m, n - 1)
    reverseString(s, 0, n - 1)
    return s

if __name__ == '__main__':
    s = 'abcdef'
    print s
    print ''.join(leftRotateString(list(s), len(s), 2))