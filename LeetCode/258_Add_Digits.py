#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '30/10/2016'
"""


def add_digit(num):
    if num == 0:
        return 0
    else:
        return num % 9 or 9
