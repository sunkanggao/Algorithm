# -*- utf-8 -*-

"""
https://www.nowcoder.com/test/question/5a0a2c7e431e4fbbbb1ff32ac6e8dfa0?pid=2385858&tid=9434974
"""

num = int(raw_input())

for i in range(num):
    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    cards = raw_input().split()
    cards = [int(p) for p in cards]
    final = []
    for j in range(2 * n):
        tmp = j + 1
        for x in range(k):
            if tmp < n:
                tmp = 2 * tmp - 1
            else:
                tmp = 2 * (tmp - n)
        final[tmp - 1] = cards[j]

    for item in final:
        print item,
    print
