# -*- coding:utf-8 -*-

"""
逆波兰表达式，中缀表达式可以对应一棵二叉树，逆波兰表达式即该二叉树后续遍历的结果。
"""

def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/'


def reversePolishNotation(p):
    stack = list()
    for cur in p:
        if not isOperator(cur):
            stack.append(cur)
        else:
            b = float(stack.pop())
            a = float(stack.pop())
            if cur == '+':
                stack.append(a + b)
            elif cur == '-':
                stack.append(a - b)
            elif cur == '*':
                stack.append(a * b)
            elif cur == '/':
                stack.append(a / b)
    return stack[-1]


if __name__ == '__main__':
    p = ['2', '1', '+', '3', '*']
    print reversePolishNotation(p)