# -*- coding:utf-8 -*-

"""
给定一个无重复元素的数组A[0 ... N-1]，求找到一个该数组的局部最大值。
规定在数组边界外的值无穷小，即A[0] > A[-1]，A[N - 1] > A[N]。
局部最大值的形式化定义：
a = one of {a[i] | a[i] > a[i - 1] 且 a[i] > a[i + 1], 0 =< i =< N - 1}

定义：若子数组Array[from,...,to]满足:
      Array[from] > Array[from - 1]
      Array[to] > Array[to + 1]
称该子数组为高原数组。
若高原数组长度为1，则该高原数组的元素为局部最大值。
"""

def localMaximum(array):
    """
    返回给定数组的一个局部最大值。
    A[mid] > A[mid + 1]，子数组A[left ... mid]为高原数组。丢弃后半段：right = mid
    A[mid + 1] > A[mid]，子数组A[mid+1 ... right]为高原数组。丢弃前半段：left = mid + 1
    :param array:
    :return:
    """
    left, right = 0, len(array) - 1
    while left < right:
        mid = (left + right) / 2
        if array[mid] > array[mid + 1]:
            right = mid
        else:
            left = mid + 1   # 注意这里的+1
    return array[left]


if __name__ == '__main__':
    array = [4, 3, 1, 5, 3, 2, 1, 4, 3]
    print localMaximum(array)
