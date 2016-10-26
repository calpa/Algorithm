#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '26/10/2016'
"""


def counting_sort(arr, k):
    counter = [0] * (k + 1)
    # Count the number of each element in arr
    for i in arr:
        counter[i] += 1

    ndx = 0
    for i in xrange(len(counter)):
        while 0 < counter[i]:
            arr[ndx] = i
            ndx += 1
            counter[i] -= 1
"""
array = [4, 3, 2, 1, 4, 3, 2, 4, 3, 4]
k = 6
counting_sort(array, k)
print array
"""
