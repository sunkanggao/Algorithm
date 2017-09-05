# -*- coding: utf-8 -*-
"""
此文件中链表默认有头指针。
"""

import numpy as np

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 链表相加
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry /= 10
        return dummy.next

    # 链表部分翻转（头插法）
    def partReverse(self, pHead, m, n):
        head = pCur = pHead.next
        if m == 1:
            pPre = pCur
            pCur = pCur.next
            for i in range(n - 1):
                pNext = pCur.next
                pCur.next = head
                pPre.next = pNext
                head = pCur
                pCur = pNext
            pHead.next = head
            return pHead
        else:
            for i in range(m - 1):
                head = pCur
                pCur = pCur.next
            pPre = pCur
            pCur = pCur.next
            for i in range(m, n):
                pNext = pCur.next
                pCur.next = head.next
                head.next = pCur
                pPre.next = pNext
                pCur = pNext
            return pHead

    # 排序列表中去重（只保留一个重复元素）
    def deleteDuplicateNode(self, pHead):
        pPre = pHead.next
        while pPre:
            pCur = pPre.next
            if pCur and pPre.val == pCur.val:
                pPre.next = pCur.next
                del pCur
            else:
                pPre = pCur
        return pHead

    # 排序列表去重（删除所有重复元素）
    def deleteDuplicateNode2(self, pHead):
        pPre = pHead
        pCur = pPre.next
        while pCur:
            pNext = pCur.next
            bDup = False
            while pNext and pCur.val == pNext.val:
                pPre.next = pNext
                del pCur
                pCur = pNext
                pNext = pCur.next
                bDup = True
            if bDup:
                pPre.next = pNext
                del pCur
            else:
                pPre = pCur
            pCur = pNext
        return pHead

    # 链表划分
    def partition(self, pHead, key):
        pLeftHead = ListNode(0)
        pRightHead = ListNode(0)
        curLeft = pLeftHead
        curRight = pRightHead
        cur = pHead.next
        while cur:
            if cur.val < key:
                curLeft.next = cur
                curLeft = cur
            else:
                curRight.next = cur
                curRight = cur
            cur = cur.next
        curLeft.next = pRightHead.next
        curRight.next = None # 这句千万别忘，否则可能造成死循环
        pHead.next = pLeftHead.next
        del pLeftHead
        del pRightHead
        return pHead

    # 单链公共节点问题
    def findFirstSameNode(self, pA, pB):
        pA = pA.next
        pB = pB.next
        nA = self.calcLength(pA)
        nB = self.calcLength(pB)
        if nA > nB:
            pA, pB = pB, pA
            nA, nB = nB, nA

        # 空转nB - nA次
        for i in range(nB - nA):
            pB = pB.next

        # 齐头并进
        while pA:
            # 注意此处在C++中，若两链表相等，则内存地址也相同，python中则不是
            # C++中为：pA == pB
            if pA.val == pB.val:
                pHead = ListNode(0)
                pHead.next = pA
                return pHead
            pA = pA.next
            pB = pB.next
        return None

    # 计算链表长度
    def calcLength(self, pHead):
        l = 0
        p = pHead.next
        while p:
            p = p.next
            l += 1
        return l

    # 打印列表
    def output(self, l):
        while l.next:
            l = l.next
            if l.next:
                print l.val, '->',
            else:
                print l.val


if __name__ == '__main__':
    l1 = ListNode(0)
    for i in range(np.random.randint(1, 10)):
        p = ListNode(np.random.randint(0, 10))
        p.next = l1.next
        l1.next = p

    l2 = ListNode(0)
    for i in range(np.random.randint(1, 10)):
        p = ListNode(np.random.randint(0, 10))
        p.next = l2.next
        l2.next = p

    l3 = cur = ListNode(0)
    a = [1, 1, 2, 3, 4, 4, 4, 5]
    for i in a:
        p = ListNode(i)
        cur.next = p
        cur = cur.next


    l4 = cur = ListNode(0)
    for i in range(1, 10):
        p = ListNode(i)
        cur.next = p
        cur = cur.next

    l5 = cur = ListNode(0)
    a = [1, 2, 3, 5, 6, 7, 8]
    for i in a:
        p = ListNode(i)
        cur.next = p
        cur = p

    l6 = cur = ListNode(0)
    b = [9, 8, 6, 7, 8]
    for i in b:
        p = ListNode(i)
        cur.next = p
        cur = p

    l7 = cur = ListNode(0)
    a = [1, 1, 2, 3, 4, 4, 4, 5]
    for i in a:
        p = ListNode(i)
        cur.next = p
        cur = cur.next

    s = Solution()

    print u'*********链表相加*********'
    s.output(l1)
    s.output(l2)
    s.output(s.addTwoNumbers(l1, l2))

    print u'\n*********链表删除重复节点*********'
    s.output(l3)
    s.output(s.deleteDuplicateNode(l3))

    print u'\n*********链表部分翻转*********'
    s.output(l4)
    s.output(s.partReverse(l4, 1, 8))

    print u'\n*********链表划分*********'
    s.output(l1)
    s.output(s.partition(l1, 4))

    print u'\n*********链表删除重复节点*********'
    s.output(l7)
    s.output(s.deleteDuplicateNode2(l7))

    print u'\n*********单链公共节点问题*********'
    s.output(l5)
    s.output(l6)
    g = s.findFirstSameNode(l5, l6)
    if g is not None:
        s.output(g)
    else:
        print 'None'