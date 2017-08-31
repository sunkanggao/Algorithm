# -*- coding: utf-8 -*-

"""
题目描述
大家应该都会玩“锤子剪刀布”的游戏：
现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。

输入描述:
输入第1行给出正整数N（<=105），即双方交锋的次数。随后N行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。C代表“锤子”、J代表“剪刀”、B代
表“布”，第1个字母代表甲方，第2个代表乙方，中间有1个空格。

输出描述:
输出第1、2行分别给出甲、乙的胜、平、负次数，数字间以1个空格分隔。第3行给出两个字母，分别代表甲、乙获胜次数最多的手势，中间有1个空格。如果解不唯
一，则输出按字母序最小的解。

输入例子:
10
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J

输出例子:
5 3 2
2 3 5
B B
"""

def mySort(d):
    dlist = sorted(d.items(), key=lambda x: x[0])
    return sorted(dlist, key=lambda x: x[1], reverse=True)[0][0]


d1 = {'C':0, 'J':0, 'B':0}
d2 = {'C':0, 'J':0, 'B':0}
p = 0

n = int(raw_input())
for i in range(n):
    x, y = raw_input().strip().split()
    if x == 'C' and y == 'J':
        d1['C'] += 1
    elif x == 'J' and y == 'B':
        d1['J'] += 1
    elif x == 'B' and y == 'C':
        d1['B'] += 1
    elif x == 'C' and y == 'B':
        d2['B'] += 1
    elif x == 'J' and y == 'C':
        d2['C'] += 1
    elif x == 'B' and y == 'J':
        d2['J'] += 1
    elif x == y:
        p += 1

d1w = sum(d1.values())
d2w = sum(d2.values())
print d1w, p, d2w
print d2w, p, d1w
print mySort(d1), mySort(d2)