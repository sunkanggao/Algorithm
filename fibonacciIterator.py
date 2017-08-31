# -*- coding:utf-8 -*-

import time

__metaclass__ = type

class Fibs:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        fibs = self.a
        self.n += 1
        if self.n > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fibs

if __name__ == '__main__':
    t = time.time()
    fibs = Fibs(30)
    print list(fibs),
    print t - time.time()
