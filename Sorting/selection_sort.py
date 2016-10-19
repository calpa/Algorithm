#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '18/10/2016'
"""


def selection_sort(arr):
    # n: the number of elements to sort
    n = len(arr)
    for i in xrange(0, n):
        smallest = i
        for x in xrange(i, n):
            if arr[smallest] > arr[x]:
                smallest = x
        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr


# Testing:
array = [1, 3, 2, 4, 5, 10, 9, 8, 7]
print selection_sort(array)
