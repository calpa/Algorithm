#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '20/10/2016'
"""


def quick_sort(arr, p, r):

    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)


def partition(arr, p, r):
    q = p
    for u in xrange(p, r):
        if arr[u] <= arr[r]:
            arr[q], arr[u] = arr[u], arr[q]
            q += 1

    arr[q], arr[r] = arr[r], arr[q]
    return q

array = [12, 7, 14, 9, 10, 11]

quick_sort(array, 0, len(array) - 1)

print array