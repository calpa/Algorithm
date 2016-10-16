#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '16/10/2016'
"""

nums = [0, 1, 0, 3, 12]


def move_zeroes(nums):
    j = 0

    for i in xrange(0, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums  # Delete this

print move_zeroes(nums)
