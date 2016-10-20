#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '20/10/2016'
"""


def two_sum(nums, total):
    hashtable = {}
    for i in xrange(0, len(nums)):
        if total - nums[i] in hashtable:
            return [hashtable[total - nums[i]], i]
        hashtable[nums[i]] = i


arr = [2, 5, 7, 9]
target = 9

print two_sum(arr, target)
