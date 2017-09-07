# -*- coding:utf-8 -*-

def moveOne(f, t):
    print f, '->', t


def move(f, t, aux, n):
    """
    :param f: 起始柱
    :param t: 目标柱
    :param aux: 辅助柱
    :param n: 汉诺塔层数
    :return:
    """
    if n == 1:
        moveOne(f, t)
        return
    move(f, aux, t, n - 1)
    moveOne(f, t)
    move(aux, t, f, n - 1)


if __name__ == '__main__':
    n = 3
    move('A', 'C', 'B', n)
