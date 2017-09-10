# -*- coding:utf-8 -*-

def rotateArrayMinimum(array):
    """
    寻找旋转数组中的最小值（数组中没有重复值），例如：4,5,6,7,0,1,2
    方法：二分查找
    :param array:
    :return:
    """
    left, right = 0, len(array) - 1
    while left < right:
        mid = (left + right) / 2
        if array[mid] > left:    # 最小值在右半部分
            left = mid + 1    # 注意此处的+1
        elif array[mid] < left:    # 最小部分在左半部分
            right =mid
    return array[left]


if __name__ == '__main__':
    array = [4, 5, 6, 7, 0, 1, 2]
    print rotateArrayMinimum(array)