# -*- coding:utf-8 -*-

def inPost2Pre(pInOrder, pPostOrder, nLength, pPreOrder, nIndex):
    """
    根据中序和后序序列，推出前序序列。
    分治递归实现，后序遍历的最后一个值为前序遍历的第一个值，根据中序遍历确定左右子树。
    注意：在C++中，nIndex为引用类型，但python中无引用类型，
    1.对于不可变对象（比如字符串、整型）作为函数参数，相当于C系语言的值传递；
    2.对于可变对象（比如列表List）作为函数参数，相当于C系语言的引用传递。
    故在python中为了实现引用传递功能，nIndex用list表示。

    :param pInOrder: 中序遍历序列
    :param pPostOrder: 后续遍历序列
    :param nLength: 当前序列的长度
    :param pPreOrder: 前序遍历序列
    :param nIndex: 前序遍历序列的当前索引
    :return: 前序遍历序列
    """
    if nLength <= 0:
        return
    if nLength == 1:
        pPreOrder[nIndex[0]] = pPostOrder[0]
        nIndex[0] += 1
        return
    root = pPostOrder[nLength - 1]
    pPreOrder[nIndex[0]] = root
    nIndex[0] += 1
    nRoot = 0
    while nRoot < nLength:
        if pInOrder[nRoot] == root:
            break
        nRoot += 1
    inPost2Pre(pInOrder, pPostOrder, nRoot, pPreOrder, nIndex)
    inPost2Pre(pInOrder[nRoot+1 :], pPostOrder[nRoot :], nLength-nRoot-1, pPreOrder, nIndex)


if __name__ == '__main__':
    pInOrder = "ADEFGHMZ"
    pPostOrder = "AEFDHZMG"
    size = len(pInOrder)
    pPreOrder = [0] * size
    nIndex = [0]
    inPost2Pre(list(pInOrder), list(pPostOrder), size, pPreOrder, nIndex)
    for i in pPreOrder:
        print i,
    print