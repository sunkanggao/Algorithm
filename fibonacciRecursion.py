# -*- coding:utf-8 -*-
import time

# 递归
def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)

# 递归，并初始化，经验证，此方法是所有方法中最快的。
memo = {0:0, 1:1}
def fib2(n):
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]

# 迭代
def fib3(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a


t = time.time()
print fib1(30)
print time.time() - t

t = time.time()
print fib2(300)
print time.time() - t

t = time.time()
print fib3(10)
print time.time() - t

