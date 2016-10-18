#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '14/10/2016'
"""


def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursion
    else:
        return n + factorial(n-1)

# Test
for i in xrange(0, 10):
    print factorial(i),  # 1 1 3 6 10 15 21 28 36 45
