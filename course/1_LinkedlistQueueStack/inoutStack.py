# -*- coding:utf-8 -*-

"""
给定无重复元素的两个等长数组，分别表述入栈序列和出栈序列，
请问，这样的出栈序列是否可行。
"""

def isPossible(strIn, strOut):
    stack = list()
    idxIn = 0
    idxOut = 0
    while idxOut != len(strOut):
        if len(stack) != 0 and stack[-1] == strOut[idxOut]:
            stack.pop()
            idxOut += 1
        else:
            if idxIn == len(strIn):
                return False
            stack.append(strIn[idxIn])
            idxIn += 1
    return True

if __name__ == '__main__':
    strIn = 'ABCDEFG'
    strOut = 'BAEDFGC'
    print isPossible(strIn, strOut)
