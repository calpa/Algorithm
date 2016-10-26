#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '26/10/2016'
"""


def print_array(arr):
    for i in xrange(len(arr)):
        print arr[i],
    print ""


def insertion_sort(arr):
    e = arr[-1]
    i = len(arr) - 1

    while i >= 0:
        if arr[i] > e:
            arr[i+1] = arr[i]
            print_array(arr)
        if arr[i] < e:
            arr[i+1] = e
            break

        if i == 0:  # If all elements before the last element > last element
            arr[0] = e

        i -= 1

    print_array(arr)

array = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertion_sort(array)
