#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '18/10/2016'
"""


def binary_search(arr, n, x):
    p = 1
    r = n
    while p <= r:  # Increase p until p reaches the end
        q = (p+r)/2
        if arr[q] == x:
            return q
        if arr[q] > x:
            r = q - 1
        elif arr[q] < x:
            p = q + 1

    return "NOT-FOUND"


def recursive_binary_search(arr, p, r, x):
    if p > r:
        return "NOT-FOUND"
    else:
        q = (p+r)/2  # Middle
        if arr[q] == x:
            return q
        elif arr[q] > x:
            return recursive_binary_search(arr, p, q-1, x)
        elif arr[q] < x:
            return recursive_binary_search(arr, q+1, r, x)


def make_arr(target):
    # Make a long arr
    temp = []
    for x in xrange(target):
        temp.append(x)
    return temp

"""
Testing:
total = 10000000

arr = make_arr(total)

print binary_search(arr, total, 501)
print recursive_binary_search(arr, 0, total, 501)
"""