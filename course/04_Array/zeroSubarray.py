# -*- coding: utf-8 -*-

"""
对于长度为N的数组A，求连续子数组的和最接近0的值。
"""

def zeroSubarray(array):
    """
    申请比A长1的空间sum[-1, 0, ..., N-1]，sum[i]是前i项的和，sum[-1] = 0。
    显然原数组中的某个子序列A[i,...,j]的和=sum[j] - sum[i-1]。
    对sum进行排序，相邻做差取最小值。
    时间复杂度：求sum：O(N)，对sum排序：O(NlogN)，
    空间复杂度：O(N)。
    :param array:
    :return:
    """
    size = len(array)
    sums = [0] * (size + 1)
    for i in range(size):
        sums[i + 1] = sums[i] + array[i]
    sums = sorted(sums)
    minimum = sums[1] - sums[0]
    for i in range(len(sums) - 1):
        cur = sums[i + 1] - sums[i]
        minimum = min(minimum, cur)
    return minimum


if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    print zeroSubarray(array)
