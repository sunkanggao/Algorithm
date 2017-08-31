# -*- coding:utf-8 -*-

"""
小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
1、将a_i放入b序列的末尾
2、逆置b序列
小易需要你计算输出操作n次之后的b序列。
输入描述:
输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。


输出描述:
在一行中输出操作n次之后的b序列,以空格分割,行末无空格。

输入例子1:
4
1 2 3 4

输出例子1:
4 2 1 3
"""

n = int(raw_input())
s = map(int, raw_input().split())
s.reverse()
p = [0] * len(s)
l = 0
r = len(s) - 1
for index, i in enumerate(s):
    if index % 2 == 0:
        p[l] = i
        l += 1
    else:
        p[r] = i
        r -= 1
for i in range(len(p) - 1):
    print p[i],
print p[len(p) - 1]
