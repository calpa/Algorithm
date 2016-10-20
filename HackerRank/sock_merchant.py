#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '20/10/2016'
"""


def sock_merchant():
    n = raw_input()  # No use in Python
    c = map(int, raw_input('').strip().split(' '))  # 10 20 20 10 10 30 50 10 20

    s = list(set(c))

    total = 0

    for x in xrange(len(s)):
        if c.count(s[x]) > 1:
            total += c.count(s[x]) / 2

    print total

sock_merchant()
