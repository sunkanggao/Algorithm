# -*- coding:utf-8 -*-

def canPostOrder(a):
    """
    判断一个数组是否可能是一棵二叉查找树后序遍历的结果。
    由于后序遍历的最后一个元素为根节点，根据该节点，将数组分成前后两段，
    使得前半段都小于根节点，后半段都大于根节点；如果不存在这样的划分，
    则不可能是后续遍历的结果。
    :param a: 待判断序列
    :return:
    """
    size = len(a)
    if size <= 1:
        return True
    root = a[size - 1]
    nleft = 0
    while nleft < size - 1:
        if a[nleft] > root:
            break
        nleft += 1
    nright = size - 2
    while nright >= 0:
        if a[nright] < root:
            break
        nright -= 1
    if nright != nleft - 1:
        return False

    return canPostOrder(a[0:nleft]) and canPostOrder(a[nleft:-1])


if __name__ == '__main__':
    # a = [1, 2, 5, 4, 3]
    # a = [5, 4, 3, 2, 1]
    a = [3, 5, 1, 4, 2]
    print canPostOrder(a)
