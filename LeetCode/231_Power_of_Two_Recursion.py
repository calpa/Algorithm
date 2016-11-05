#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '5/11/2016'
"""


def power_two(num):
    # 36ms...
    while num > 0 and num % 2 == 0:
        num /= 2
    return num == 1
