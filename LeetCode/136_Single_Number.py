#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '22/11/2016'
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        0 ^ 0 => 0
        0 ^ 1 => 1
        1 ^ 0 => 1
        1 ^ 1 => 0
        """
        result = 0
        for i in nums:
            result ^= i
        return result
