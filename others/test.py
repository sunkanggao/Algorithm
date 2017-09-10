# -*- coding:utf-8 -*-
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
        return True


def is_ugly(n):
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and is_prime(i):
            if i != 2 and i != 3 and i != 5:
                return False
    return True

if __name__ == '__main__':
    n = int(raw_input())
    cur = 1
    flag = 1
    i = 1
    while flag != n:
        i += 1
        if is_ugly(i):
            cur = i
            flag += 1

    print cur