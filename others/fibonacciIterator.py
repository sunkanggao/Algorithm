# -*- coding:utf-8 -*-

import time

__metaclass__ = type

class Fibs:
    """
    斐波那契数列迭代器
    """
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return self.a
        raise StopIteration()


if __name__ == '__main__':
    t = time.time()
    for i in Fibs(5):
        print i
    print t - time.time()
