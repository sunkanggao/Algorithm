# -*- coding:utf-8 -*-

"""
字符串查找问题
给定文本串text和模式串pattern，从文本串text中找出
模式串pattern第一次出现的位置。
BF（暴力）求解：时间复杂度O(M*N)，空间复杂度O(1)
KMP求解：时间复杂度O(M+N)，空间复杂度O(M)
"""

def getNext(p):
    pLen = len(p)
    nextArray = [0] * pLen
    nextArray[0] = -1
    k = -1
    j = 0
    while j < pLen - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            nextArray[j] = k
        else:
            k = nextArray[k]
    return nextArray


def getNext2(p):
    pLen = len(p)
    nextArray = [0] * pLen
    nextArray[0] = -1
    k = -1
    j = 0
    while j < pLen - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            if p[j] == p[k]:
                nextArray[j] = nextArray[k]
            else:
                nextArray[j] = k
        else:
            k = nextArray[k]
    return nextArray


def KMP(text, pattern):
    ans = -1
    i = 0
    j = 0
    text_len = len(text)
    pattern_len = len(pattern)
    pNext = getNext2(pattern)
    while i < text_len:
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = pNext[j]
        if j == pattern_len:
            ans = i - pattern_len
            break
    return ans


if __name__ == '__main__':
    text = 'abcabcabcbababcbaab'
    pattern = 'abcba'
    print KMP(text, pattern)