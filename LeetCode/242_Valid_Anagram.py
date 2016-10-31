#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '31/10/2016'
"""


def valid_anagram(s, t):
    data = {}
    data2 = {}
    if len(s) != len(t):
        return False

    for char in set(s):
        data[char] = s.count(char)
        data2[char] = t.count(char)
    return data == data2

"""
Anagram means change the order of the string only.
aacc, ccaa => True
abcde, abcdef => False
"""
print valid_anagram('aacc', 'ccaa')
