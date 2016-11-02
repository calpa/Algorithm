#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '2/11/2016'
"""


def find_the_difference(s, t):
    # Create an empty set first
    char_set = set()
    for char in set(t):
        if char in char_set:
            continue
        # Difference:
        if s.count(char) != t.count(char):
            return char

        char_set.add(char)
