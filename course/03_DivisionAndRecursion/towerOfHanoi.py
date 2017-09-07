# -*- coding:utf-8 -*-

"""
n个盘子看做前n-1个盘子和最后一个盘子组成。
将前n-1个盘子移动到aux柱上: 2^(n-1)-1
将最大的盘子移动到t柱上: 1
将前n-1个盘子移动到t柱上: 2^(n-1)-1
"""

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


def calc(s, size, f, t, aux):
    """
    给定从小到大的n个盘子，它们散乱的位于A、B、C柱上，
    问这一状态是否是将这n个盘子从A借助B移动到C的必经状态？
    如果是，返回是第几个状态，如果不是，返回-1。
    :param s: 盘子状态序列
    :param size: 当前盘子状态序列长度
    :param f: 起始柱
    :param t: 目标柱
    :param aux: 辅助柱
    :return: 状态的序号
    """
    if size == 0:
        return 0

    # 情况一：最大盘子位于辅助柱，为不可能情况
    if s[size - 1] == aux:
        return -1

    # 情况二：最大盘子位于目标柱，返回2^(n-1)-1+1+n
    if s[size - 1] == t:
        n = calc(s, size - 1, aux, t, f)
        if n == -1:
            return -1
        return 1 << (size - 1) + n

    # 情况三：最大盘子位于起始柱，返回n
    return calc(s, size - 1, f, aux, t)


if __name__ == '__main__':
    n = 3
    move('A', 'C', 'B', n)

    s = 'ABC'
    print calc(s, 3, 'A', 'C', 'B')

    s = 'AAC'
    print calc(s, 3, 'A', 'C', 'B')