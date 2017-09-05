# -*- coding:utf-8 -*-

"""
给定无向连通图，输出其最短路径的条数。
"""

import Queue
import numpy as np

N = 16

def calc(G):
    # 每个节点第几步可以到达
    step = np.zeros(N)
    # 到每个节点有几种走法
    stepNumber = np.zeros(N)
    stepNumber[0] = 1
    q = Queue.Queue()
    q.put(0)
    while not q.empty():
        f = q.get()
        s = step[f] + 1
        for i in range(1, N):
            if G[f, i] == 1:
                if step[i] == 0 or step[i] > s:
                    step[i] = s
                    stepNumber[i] = stepNumber[f]
                    q.put(i)
                elif step[i] == s:
                    stepNumber += stepNumber[f]
    return stepNumber[N - 1]


if __name__ == '__main__':
    G = np.zeros((N, N))
    G[0, 1] = G[0, 4] = 1
    G[1, 5] = G[1, 0] = G[1, 2] = 1
    G[2, 1] = G[2, 6] = G[2, 3] = 1
    G[3, 2] = G[3, 7] = 1
    G[4, 0] = G[4, 5] = 1
    G[5, 1] = G[5, 4] = G[5, 6] = G[5, 9] = 1
    G[6, 2] = G[6, 5] = G[6, 7] = G[6, 10] = 1
    G[7, 3] = G[7, 6] = 1
    G[8, 9] = G[8, 12] = 1
    G[9, 8] = G[9, 13] = G[9, 10] = 1
    G[10, 9] = G[10, 14] = G[10, 11] = 1
    G[11, 10] = G[11, 15] = 1
    G[12, 8] = G[12, 13] = 1
    G[13, 9] = G[13, 12] = G[13, 14] = 1
    G[14, 10] = G[14, 13] = G[14, 15] = 1
    G[15, 11] = G[15, 14] = 1

    print calc(G)


