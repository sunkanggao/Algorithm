# -*- coding:utf-8 -*-

"""
输入两个非负10进制整数A和B(<=230-1)，输出A+B的D (1 < D <= 10)进制数。

输入格式：
输入在一行中依次给出3个整数A、B和D。

输出格式：
输出A+B的D进制数。

输入样例：
123 456 8
输出样例：
1103
"""

a, b, d = map(int, raw_input().split())
n = a + b
r = ''
while True:
    n, i = divmod(n, d)
    r += str(i)
    if n == 0:
        break
print r[::-1]
