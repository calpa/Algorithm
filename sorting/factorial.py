#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '14/10/2016'
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
