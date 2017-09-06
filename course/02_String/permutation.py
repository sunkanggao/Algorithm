# -*- coding:utf-8 -*-


def permutation(a, n):
    """
    字符串的全排列（字符无重复）
    时间复杂度为O(n!)
    :param a: 输入字符串
    :param n: 当前子串全排列起点
    :return:
    """
    size = len(a)
    if n == size - 1:
        print ''.join(a)
        return
    for i in range(n, size):
        a[i], a[n] = a[n], a[i]
        permutation(a, n + 1)
        a[i], a[n] = a[n], a[i]    # 重新得到原字符串


def permutation2(a, n):
    """
    字符串全排列（字符有重复）
    时间复杂度为O((n+1)!)
    :param a: 输入字符串
    :param n: 当前子串全排列起点
    :return:
    """
    size = len(a)
    if n == size - 1:
        print ''.join(a)
        return
    for i in range(n, size):
        # a[i]是否与[n, i)重复
        if isDuplicate(a, n, i):
            continue
        a[i], a[n] = a[n], a[i]
        permutation2(a, n + 1)
        a[i], a[n] = a[n], a[i]


def isDuplicate(a, n, t):
    while n < t:
        if a[n] == a[t]:
            return True
        n += 1
    return False


def permutation3(a, n):
    """
    字符串全排列（字符有重复，空间换时间）
    时间复杂度O(n!)
    :param a: 输入字符串
    :param n: 当前子串全排列起点
    :return:
    """
    size = len(a)
    if n == size - 1:
        print ''.join(a)
        return
    dup = [0] * 256
    for i in range(n, size):
        if dup[ord(a[i])] == 1:
            continue
        dup[ord(a[i])] = 1
        a[i], a[n] = a[n], a[i]
        permutation3(a, n + 1)
        a[i], a[n] = a[n], a[i]



if __name__ == '__main__':
    s1 = '1234'
    print '*********%s***********' % s1
    permutation(list(s1), 0)

    s2 = '1223'
    print '*********%s***********' % s2
    permutation2(list(s2), 0)

    print '*********%s***********' % s2
    permutation3(list(s2), 0)
