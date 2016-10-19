#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '18/10/2016'
"""


def insertion_sort(arr):
    for i in xrange(1, len(arr)):  # Start from the second
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


# Testing:
array = [12, 9, 3, 7, 14, 11]
print insertion_sort(array)
