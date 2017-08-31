# -*- coding: utf-8 -*-
import time

def fibs(n):
    a, b = 0 ,1
    for i in xrange(n):
        a, b = b, a + b
        yield a

if __name__ == "__main__":
    t = time.time()
    f = fibs(10)
    for i in f:
        print i,
    print time.time() - t