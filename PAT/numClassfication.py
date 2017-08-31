# -*- coding:utf-8 -*-
"""
题目描述
给定一系列正整数，请按要求对数字进行分类，并输出以下5个数字：



A1 = 能被5整除的数字中所有偶数的和；

A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；

A3 = 被5除后余2的数字的个数；

A4 = 被5除后余3的数字的平均数，精确到小数点后1位；

A5 = 被5除后余4的数字中最大数字。

输入描述:
每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N，随后给出N个不超过1000的待分类的正整数。数字间以空格分隔。


输出描述:
对给定的N个正整数，按题目要求计算A1~A5并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。

若其中某一类数字不存在，则在相应位置输出“N”。

输入例子:
13 1 2 3 4 5 6 7 8 9 10 20 16 18

输出例子:
30 11 2 9.7 9
"""

nums = [int(i) for i in raw_input().strip().split()]
n = nums.pop(0)

d = {'A1':[], 'A2':[], 'A3':[], 'A4':[], 'A5':[]}
for i in nums:
    if i % 5 == 0:
        d['A1'].append(i)
    elif i % 5 == 1:
        d['A2'].append(i)
    elif i % 5 == 2:
        d['A3'].append(i)
    elif i % 5 == 3:
        d['A4'].append(i)
    elif i % 5 == 4:
        d['A5'].append(i)
    else:
        pass

sums = 0
if len(d['A1']):
    for i in d['A1']:
        if i % 2 == 0:
            sums += i
    if sums == 0:
        print 'N',
    else:
        print sums,
else:
    print 'N',

sums = 0
if len(d['A2']):
    for index, i in enumerate(d['A2']):
        sums += i * (-1) ** index
    print sums,
else:
    print 'N',

if len(d['A3']):
    print len(d['A3']),
else:
    print 'N',

if len(d['A4']):
    print round(sum(d['A4']) * 1.0 / len(d['A4']), 1),
else:
    print 'N',

if len(d['A5']):
    print max(d['A5'])
else:
    print 'N'