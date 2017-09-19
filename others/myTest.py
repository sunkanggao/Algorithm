# -*- coding:utf-8 -*-

class MyTest(object):
    """My class test."""

    age = 17
    score = [100, 98, 99, 100, 98]
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @staticmethod
    def myHome():
        print "I'm from Shaoxing!"

    @classmethod
    def hello(cls):
        print 'hello world'
        print 'hello() is part of class: ', cls.__name__

    @property
    def name(self):
        return self.__name

class Spring(object):
    __slots__ = ('05_Tree', 'flower')

print dir(Spring)


t = MyTest('Kanggao')
print '------------------------------'
for items in MyTest.__dict__.items():
    print items[0], ':', items[1]
print '------------------------------'
MyTest.myHome()
MyTest.hello()

print t.getName()
print t.name

t.age += 1
print t.age
print MyTest.age

t.score.append(100)
print t.score
print MyTest.score

t.sex = 'male'
print t.sex