# -*- coding:utf-8 -*-

"""
给定字串，仅有“(){}[]”六个字符组成，设计算法，判断该字符串是否有效。
"""

def isLeftBracket(c):
    return c == '(' or c == '{' or c == '['


def isMatch(a, b):
    if a == '(':
        return b == ')'
    if a == '[':
        return b == ']'
    if a == '{':
        return '}'


def bracketMatching(p):
    stack = list()
    for cur in p:
        if isLeftBracket(cur):
            stack.append(cur)
        else:
            if len(stack) == 0 or not isMatch(stack.pop(), cur):
                return False
    return len(stack) == 0


if __name__ == '__main__':
    p = '(({})[])[()]'
    if bracketMatching(p):
        print p, u'括号匹配'
    else:
        print p, u'括号不匹配'
