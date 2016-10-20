#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '20/10/2016'
"""


def jumping(arr):
    i = 0
    counter = 0
    while i < len(arr)-1:  # Befor Last Cloud
        if i + 2 < len(arr):
            check = i + 2
        else:
            check = i + 1

        if arr[check] != 1:
            i += 2
        else:
            i += 1
        counter += 1
    return counter

nums = '0 0 1 0 0 1 0'

array = map(int, nums.split(' '))

print jumping(array)
