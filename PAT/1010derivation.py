# -*- coding:utf-8 -*-

"""
设计函数求一元多项式的导数。（注：xn（n为整数）的一阶导数为n*xn-1。）

输入格式：以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过1000的整数）。数字间以空格分隔。

输出格式：以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格。注意“零多项式”的指数和系数都是0，但是表示为“0 0”。

输入样例：
3 4 -5 2 6 1 -2 0
输出样例：
12 3 -10 1 6 0

"""

s = map(int, raw_input().split())
result = []
for i in range(0, len(s), 2):
    if s[i] * s[i + 1]:
        result.append(s[i] * s[i + 1])
        result.append(s[i + 1] - 1)

if len(result) != 0:
    for i in range(len(result) - 1):
        print result[i],
    print result[len(result) - 1]
else:
    print 0, 0
