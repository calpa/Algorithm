#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '16/10/2016'
"""


def diff(n):
    # Equation 1: sum of n^2
    # Equation 2: sum of 1+2+...+n => (1+n)^2
    # Derived from Equation 1 and Equation 2
    return n*(n+1)*(n-1)*(3*n+2)/12

print diff(3)
