#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '26/10/2016'
"""

"""
Input:
10
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the
"""

m = int(raw_input(''))

arr = [0] * 100
count = 0

for i in xrange(m):
    num, word = raw_input('').split(' ')
    arr[int(num)] += 1


for j in xrange(100):
    count += arr[j]
    print count,
