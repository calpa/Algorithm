#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '15/11/2016'
"""


def isAnagram(self, s, t):
    # HashTable
    hash = {}
    if len(s) != len(t):
        return False

    for i in s:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for j in t:
        if j in hash:
            if hash[j] >= 1:
                hash[j] -= 1
            else:
                return False
        else:
            return False
    return True
