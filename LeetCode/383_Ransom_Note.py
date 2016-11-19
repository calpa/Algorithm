#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '19/11/2016'
"""


def ransom_note(ransomNote, magazine):
    hash = {}
    for i in magazine:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for char in ransomNote:
        if char in hash:
            if hash[char] > 0:
                hash[char] -= 1
            else:
                return False
        else:
            return False

    return True
