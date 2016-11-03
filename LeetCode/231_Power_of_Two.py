#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '3/11/2016'
"""


def power_of_two(number):
    # 1: 001, 2: 010, 3: 011, 4: 100, 5: 101
    # If number is 4, then number - 1 is 3:
    # Use & operator
    # 100 & 011 == 000
    # So we need ! (001 & 010)

    return (number > 0) and not (number & (number - 1))

print power_of_two(2)
