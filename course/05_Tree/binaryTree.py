# -*- coding:utf-8 -*-

class Node:
    """
    实现一棵二叉搜索树
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        """
        插入节点
        :param data: 插入值
        :return:
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            print 'This node is already in the tree!'


    def search(self, data, parent=None):
        """
        查找某元素是否在二叉树中，并返回该元素所在节点以及它的双亲节点
        :param data: 查找值
        :param parent: 记录双亲节点
        :return:
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.search(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.search(data, self)
        else:
            return self, parent


    def delete(self, data):
        """
        删除节点
        :param data:
        :return:
        """
        node, parent = self.search(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # 如果该节点下没有子节点，可直接删除
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                # 如果该节点下只有一个子节点，则让子节点上移替换该节点
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del n
            else:
                # 如果该节点下有两个子节点，则寻找它右子树的最左节点（或左子树的最右节点）替代该节点
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left is successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                del successor


    def compare_trees(self, node):
        "比较两棵树"
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.compare_trees(node.right)
        return res


    def preOrder(self, visit):
        """
        前序遍历打印树
        :return:
        """
        visit(self)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()


    def inOrder(self):
        """
        中序遍历打印树
        :return:
        """
        if self.left:
            self.left.inOrder()
        print self.data,
        if self.right:
            self.right.inOrder()


    def postOrder(self):
        """
        后序遍历打印树
        :return:
        """
        if self.left:
            self.left.postOrder(),
        if self.right:
            self.right.postOrder()
        print self.data,


    def treeGraph(self, indent):
        """
        图像化输出二叉树
        :param indent:
        :return:
        """
        if self.right:
            self.right.treeGraph(indent+4)
        print "%*d" % (indent, self.data)
        if self.left:
            self.left.treeGraph(indent+4)


    def tree_data(self):
        """
        二叉树数据结构，中序遍历生成器
        :return:
        """
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right


    def children_count(self):
        """
        判断某一节点的子节点数
        :return:
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt


def print_data(node):
    print node.data,


if __name__ == '__main__':
    node = Node(8)
    data = [10, 7, 4, 9, 1, 11, 5, 6]
    for i in data:
        node.insert(i)
    print '原二叉树：'
    node.treeGraph(indent=0)
    print '\n前序遍历：',
    node.preOrder(print_data)
    print '\n中序遍历：',
    node.inOrder()
    print '\n后序遍历：',
    node.postOrder()
    print '\n删除树节点8：'
    node.delete(8)
    node.treeGraph(indent=0)
    for i in node.tree_data():
        print i,