#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '20/10/2016'
"""


def repeated_string(s, n):
    # s = string 'aba'
    # n = total length 10

    front = (n // len(s)) * s.count('a')  # 10/3 = 3
    remaining = s[:(n % len(s))].count('a')  # 1 < 3
    return front + remaining

# Testing
print repeated_string('aba', 100000)
