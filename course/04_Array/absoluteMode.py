# -*- coding:utf-8 -*-

"""
定义：给定N个数，称出现次数最多的数为众数；若某众数出现的次数大于N/2，称该众数为绝对众数。
"""


def absoluteMode(array):
    """
    给定一个数组，返回该数组的绝对众数。（最多只有一个）
    方法：删除数组中两个不同的数，绝对众数不变。
    :param array: 给定数组
    :return: 返回该数组的绝对众数
    """
    m = array[0]    # 候选绝对众数
    count = 0       # 出现次数
    for i in range(len(array)):
        if count == 0:
            m = array[i]
            count = 1
        elif m != array[i]:
            count -= 1     # count--表示删除一个绝对众数，i++表示删除当前数
        else:              # if m == array[i]
            count += 1
    return m


def mode(array):
    """
    给定一个数组，返回该数组的众数（查找出现次数超过N/3次
    的所有可能数）。一个数组中的1/3众数不会超过2个。
    方法：任意删除数组中的三个不相同的数，其中一个为1/3众数，则1/3众数不变。
    :param array: 给定数组
    :return: 返回该数组的1/3众数
    """
    cm, cn = 0, 0
    m = n = array[0]
    for i in range(len(array)):
        if cm == 0:
            m = array[i]
            cm = 1
        elif cn == 0:
            n = array[i]
            cn = 1
        elif array[i] == m:
            cm += 1
        elif array[i] == n:
            cn += 1
        else:   # 同时删除a[i], m, n
            cm -= 1
            cn -= 1
    result = []
    cm = cn = 0
    for i in range(len(array)):
        if array[i] == m:
            cm += 1
        elif array[i] == n:
            cn += 1
    if cm > len(array) / 3:
        result.append(m)
    if cn > len(array) / 3:
        result.append(n)

    return result


if __name__ == '__main__':
    array = [8,8,1,1,1,8,1,1,6,1,8]
    print absoluteMode(array)

    array = [1,2,3,2,5,2,2,3,3,2,3]
    print mode(array)
