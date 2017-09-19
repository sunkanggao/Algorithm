# -*- coding:utf-8 -*-
from binaryTree import Node

def reverse(node):
    """
    二叉树翻转
    :param node: 根节点
    :return:
    """
    node.left, node.right = node.right, node.left
    if node.left:
        reverse(node.left)
    if node.right:
        reverse(node.right)


if __name__ == '__main__':
    node = Node(6)
    data = [9, 5, 2, 1, 3, 4, 7]
    for i in data:
        node.insert(i)
    node.treeGraph(indent=0)
    node.inOrder()
    print
    node.postOrder()
    print
    reverse(node)
    node.treeGraph(indent=0)
    node.inOrder()
    print
    node.postOrder()