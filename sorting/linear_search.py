#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '14/10/2016'
"""


def linear_search(arr, n, x):
    answer = 'NOT-FOUND'
    for i in xrange(0, n):
        if arr[i] == x:
            answer = i
    return answer


def better_linear_search(arr, n, x):
    for i in xrange(0, n):
        if arr[i] == x:
            return i
    return 'NOT-FOUND'


def sentinel_linear_search(arr, n, x):
    last = arr[n]
    arr[n] = x
    i = 1
    while arr[i] != x:
        i += 1
    arr[n] = last
    if i < n or arr[n] == x:
        return i
    else:
        return "NOT-FOUND"