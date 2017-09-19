# -*- coding:utf-8 -*-

def inPre2Post(pInorder, pPreOrder, nLength, pPostOrder, nIndex):
    """
    根据中序和前序确定后续序列。详细参考inPost2Pre.py。
    :param pInorder:
    :param pPreOrder:
    :param nLength:
    :param pPostOrder:
    :param nIndex:
    :return:
    """
    if nLength <= 0:
        return
    if nLength == 1:
        pPostOrder[nIndex[0]] = pPreOrder[0]
        nIndex[0] += 1
        return
    root = pPreOrder[0]
    nRoot = 0
    while nRoot < nLength - 1:
        if pInorder[nRoot] == root:
            break
        nRoot += 1
    inPre2Post(pInorder, pPreOrder[1:], nRoot, pPostOrder, nIndex)
    inPre2Post(pInorder[nRoot+1 :], pPreOrder[nRoot+1 :], nLength-nRoot-1, pPostOrder, nIndex)
    pPostOrder[nIndex[0]] = root
    nIndex[0] += 1


if __name__ == '__main__':
    pInorder = "ADEFGHMZ"
    pPreorder = "GDAFEMHZ"
    size = len(pInorder)
    pPostOrder = [0] * size
    nIndex = [0]
    inPre2Post(list(pInorder), list(pPreorder), size, pPostOrder, nIndex)
    for i in pPostOrder:
        print i,