# -*- coding:utf-8 -*-

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):

    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`x * s`[::-1])
        return s * r * (r < 2**31)


if __name__ == '__main__':
    s = Solution()
    print s.reverse(-344)
