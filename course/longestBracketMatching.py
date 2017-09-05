# -*- coding:utf-8 -*-

"""
给定字符串，仅包含左括号‘(’和右括号‘)’，它可能不是括号匹配的，设计算法，
找出最长匹配的括号子串，返回该子串的长度。
"""

def longestBracketMatching(p):
    answer = 0
    start = -1
    stack = list()
    for idx, cur in enumerate(p):
        if cur == '(':
            stack.append(idx)
        else:
            if len(stack) == 0:
                start = idx
            else:
                stack.pop()
                if len(stack) == 0:
                    answer = max(answer, idx - start)
                else:
                    answer = max(answer, idx - stack[-1])
    return answer

if __name__ == '__main__':
    p = ')(()())(()'
    print longestBracketMatching(p)
