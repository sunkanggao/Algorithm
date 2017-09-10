# -*- coding:utf-8 -*-

"""
求数组A的连续子数组，使得该子数组的和最大。
"""

def maxContinuousSubarray(array):
    """
    动态规划，最优子问题。
    记s[i]为以A[i]结尾的数组中和最大的子数组，则
    s[i+1] = max(s[i] + A[i+1], A[i+1])
    时间复杂度：O(N)
    :param array:
    :return: 最大连续子数组的和
    """
    size = len(array)
    if size <=0:
        return 0
    sum = array[0]
    result = sum
    for i in range(1, size):
        sum = max(sum + array[i], array[i])
        result = max(result, sum)
    return result


def maxContinuousSubarray2(array):
    """
    :param array:
    :return: 返回最大连续子数组
    """
    size = len(array)
    if size <= 0:
        return 0
    left = right = 0
    sum = array[0]
    result = sum
    leftNew = 0
    for i in range(1, size):
        if sum > 0:
            sum += array[i]
        else:
            sum = array[i]
            leftNew = i
        if result < sum:
            result = sum
            left = leftNew
            right = i
    return array[left : right + 1]


if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    print maxContinuousSubarray(array)
    print maxContinuousSubarray2(array)

