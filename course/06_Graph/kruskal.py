# -*- coding:utf-8 -*-


#以全局变量X定义节点集合，即类似{'A':'A','B':'B','C':'C','D':'D'},
# 如果A、B两点联通，则会更改为{'A':'B','B':'B",...},即任何两点联通之后，两点的值value将相同。并查集。
X = dict()

#各点的初始等级均为0,如果被做为连接的的末端，则增加1
R = dict()


def make_set(point):
    X[point] = point
    R[point] = 0


def find(point):
    if X[point] != point:
        X[point] = find(X[point])
    return X[point]


def union(point1, point2):
    r1 = find(point1)
    r2 = find(point2)
    if r1 != r2:
        if R[r1] > R[r2]:
            X[r2] = r1
        else:
            X[r1] = r2
            if R[r1] == R[r2]: R[r2] += 1


def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minu_tree = set()

    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minu_tree.add(edge)
    return minu_tree


if __name__ == '__main__':
    graph = {
        'vertices' : ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges' : [
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (4, 'B', 'C'),
            (2, 'B', 'D'),
            (1, 'C', 'D')
        ]
    }

    result = kruskal(graph)
    print result