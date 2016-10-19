#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '18/10/2016'
"""


def merge_sort(x):

    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    a = merge_sort(x[:mid])
    b = merge_sort(x[mid:])
    return merge(a, b)


def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
            if a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1
    result += a[i:]
    result += b[j:]
    return result

array = [1, 3, 5, 2, 4, 6, 100, 98, 65, 45]
print merge_sort(array)
