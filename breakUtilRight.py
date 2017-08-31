# -*- coding:utf-8 -*-

while 1:
    try:
        x = raw_input('The first number: ')
        y = raw_input('The second number ')

        r = float(x) / float(y)
        print r
    except Exception, e:
        print e
        print 'Try again!'
    else:
        break