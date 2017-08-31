# -*- coding:utf-8 -*-

"""
题目描述
给定任一个各位数字不完全相同的4位正整数，如果我们先把4个数字按非递增排序，再按非递减排序，然后用第1个数字减第2个数字，将得到
一个新的数字。一直重复这样做，我们很快会停在有“数字黑洞”之称的6174，这个神奇的数字也叫Kaprekar常数。

例如，我们从6767开始，将得到

7766 - 6677 = 1089
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174
7641 - 1467 = 6174
... ...

现给定任意4位正整数，请编写程序演示到达黑洞的过程。

输入描述:
输入给出一个(0, 10000)区间内的正整数N。

输出描述:
如果N的4位数字全相等，则在一行内输出“N - N = 0000”；否则将计算的每一步在一行内输出，直到6174作为差出现，输出格式见样例,每行中间没有空行。注意每个数字按4位数格
式输出。

输入例子:
6767

输出例子:
7766 - 6677 = 1089
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174
"""
def pretty(num):
    if num >= 1000:
        return str(num)
    elif 100 <= num < 1000:
        return '0' + str(num)
    elif 10 <= num < 100:
        return '00' + str(num)
    elif 0 < num < 10:
        return '000' + str(num)

n = raw_input().strip()
n = pretty(int(n))
while True:
    a = [int(i) for i in sorted(n, reverse=True)]
    b = [int(i) for i in sorted(n)]
    aNum = 1000 * a[0] + 100 * a[1] + 10 * a[2] + a[3]
    bNum = 1000 * b[0] + 100 * b[1] + 10 * b[2] + b[3]
    cNum = aNum - bNum

    if aNum == bNum:
        print '{} - {} = 0000'.format(aNum, bNum)
        break
    else:
        print '{} - {} = {}'.format(aNum, pretty(bNum), pretty(cNum))

    if aNum -bNum == 6174:
        break

    n = pretty(cNum)