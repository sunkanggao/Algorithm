# -*- coding:utf-8 -*-

def binarySearch(array, a):
    """
    折半查找，查找一个元素在有序数组中的索引。
    时间复杂度：O(logN)
    空间复杂度：O(1)
    :param array: 有序数组
    :param a: 指定元素
    :return: 该元素在数组中的索引
    """
    nFrom, nTo= 0, len(array) - 1
    find = False
    nIndex = 0
    while nFrom <= nTo:
        nIndex = (nFrom + nTo) / 2
        if array[nIndex] == a:
            find = True
            break
        if array[nIndex] > a:
            nTo = nIndex
        else:
            nFrom = nIndex

    if find:
        return nIndex
    return -1


if __name__ == '__main__':
    array = [1, 3, 3, 4, 7, 9, 9, 10]
    print binarySearch(array, 4)