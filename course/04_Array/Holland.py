# -*- coding:utf-8 -*-

"""
荷兰国旗问题。
"""


def holland(a):
    """
    借鉴快排中partition的过程，设置三个指针：begin=cur=0, end=N-1。
    a[cur]=0: 1.若a[cur]=a[begin], cur++, begin++
              2.若a[cur]!=a[begin], swap(a[cur], a[begin]), cur++(因为此时a[cur]一定是1), begin++
    a[cur]=1: cur++
    a[cur]=2: swap(a[cur], a[end]), end--
    :param a: 给定数组
    :return:
    """
    size = len(a)
    begin = cur = 0
    end = size - 1
    while cur <= end:
        if a[cur] == 0:
            if a[cur] != a[begin]:
                a[begin], a[cur] = a[cur], a[begin]
            cur += 1
            begin += 1
        elif a[cur] == 1:
            cur += 1
        elif a[cur] == 2:
            a[cur], a[end] = a[end], a[cur]
            end -= 1


def hollandr(a):
    """
    设置begin=0, cur=end=N-1
    :param a:
    :return:
    """
    size = len(a)
    begin = 0
    cur = end = size -1
    while cur >= begin:
        if a[cur] == 0:
            a[cur], a[begin] = a[begin], a[cur]
            begin += 1
        elif a[cur] == 1:
            cur -= 1
        elif a[cur] == 2:
            a[end], a[cur] = a[cur], a[end]
            end -= 1
            cur -= 1


if __name__ == '__main__':
    array = [1, 2, 0, 1, 2, 2, 0, 1, 1, 0]
    hollandr(array)
    print array

