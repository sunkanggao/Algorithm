# -*- coding:utf-8 -*-

"""
题目描述
令Pi表示第i个素数。现任给两个正整数M <= N <= 10000，请输出PM到PN的所有素数。

输入描述:
输入在一行中给出M和N，其间以空格分隔。


输出描述:
输出从PM到PN的所有素数，每10个数字占1行，其间以空格分隔，但行末不得有多余空格。

输入例子:
5 27

输出例子:
11 13 17 19 23 29 31 37 41 43

47 53 59 61 67 71 73 79 83 89

97 101 103
"""
import math

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return  True

m, n = [int(i) for i in raw_input().strip().split()]
i, count1, count2 =2, 0, 0
while True:
    if isPrime(i):
        count1 += 1
        if count1 >= m and count1 <= n:
            count2 += 1
            if count2 % 10:
                print i,
            else:
                print i
        elif count1 > n:
            break
    i += 1
