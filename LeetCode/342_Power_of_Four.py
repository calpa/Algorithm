#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '3/11/2016'
"""


def power_of_four(number):
    # Use the same idea in power of two, plus 32 bits logic
    return number > 0 and (number & (number - 1)) == 0 and number & 0x55555555 != 0

print power_of_four(5)
print power_of_four(16)
