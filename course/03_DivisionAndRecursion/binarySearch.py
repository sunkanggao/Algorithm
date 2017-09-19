# -*- coding:utf-8 -*-

# 非递归实现二分查找
def binarySearch(a, value, size):
    left = 0
    right = size - 1
    while left <= right:
        mid = (left + right) / 2
        if a[mid] < value:
            left = mid + 1
        elif a[mid] > value:
            right = mid - 1
        else:
            return mid
    return -1

# 递归实现二分查找
def binarySearch2(a, value, left, right):
    if right < left:
        return -1
    mid = (left + right) / 2
    if a[mid] < value:
        return binarySearch2(a, value, mid + 1, right)
    elif a[mid] > value:
        return binarySearch2(a, value, left, mid - 1)
    else:
        return mid



if __name__ == '__main__':
    a = [1, 3, 6, 9, 11, 12]
    value = 3
    # print binarySearch(a, value, len(a))
    print binarySearch2(a, value, 0, len(a) - 1)