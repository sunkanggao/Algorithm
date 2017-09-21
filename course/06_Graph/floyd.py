# -*- coding:utf-8 -*-
import sys
import copy

def floyd(graph, sp, next):
    """
    Floyd算法，寻找任意两点之间的最短路径。
    :param graph: 原始图
    :param sp: 记录两点之间的最短路径长度的矩阵
    :param next: 记录直接后继
    :return:
    """
    size = len(graph)
    for i in range(size):
        for j in range(size):
            next[i][j] = j

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if sp[i][j] > sp[i][k] + sp[k][j]:
                    sp[i][j] = sp[i][k] + sp[k][j]
                    next[i][j] = next[i][k]
    return sp

def minPath(start, end, next, path):
    """
    寻找节点start到节点end的最短路径。
    :param start: 起始节点
    :param end: 目标节点
    :param next: 记录直接后继的矩阵
    :param path: 记录最短路径
    :return:
    """
    path.append(start)
    s = start
    while s != end:
        s = next[s][end]
        path.append(s)


def printPath(start, end, pLen, path):
    """
    打印路径。
    :param start: 起始节点
    :param end: 目标节点
    :param pLen: 路径长度
    :param path: 路径
    :return:
    """
    if pLen == MAX_INT:
        return
    print '(%d, %d): %4d' % (start, end, pLen),
    flag = True
    for i in path:
        if flag:
            print i,
            flag = False
        else:
            print '->', i,
    print


if __name__ == '__main__':
    N = 8
    MAX_INT = sys.maxint
    graph = [[MAX_INT] * N for i in range(N)]
    graph[0][5] = 24
    graph[0][2] = 47
    graph[0][4] = 70
    graph[1][3] = 31
    graph[1][6] = 74
    graph[1][7] = 79
    graph[2][1] = 55
    graph[2][3] = 88
    graph[2][4] = 23
    graph[2][6] = 66
    graph[3][7] = 29
    graph[4][1] = 31
    graph[4][6] = 42
    graph[5][2] = 25
    graph[5][3] = 120
    graph[6][7] = 66
    # 深拷贝graph，否则后面会改变graph。若直接sp = graph，则为浅拷贝。
    sp = copy.deepcopy(graph)
    next = [[0] * N for i in range(N)]

    floyd(graph, sp, next)
    for i in range(N):
        for j in range(N):
            path = []
            minPath(i, j, next, path)
            printPath(i, j, sp[i][j], path)
            
