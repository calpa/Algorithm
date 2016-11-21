#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '21/11/2016'
"""


def guess(num):  # guess is a pre-defined API
    answer = 1000
    if num == answer:  # Equal
        return 0
    elif num > answer:  # Larger
        return 1
    else:  # Smaller
        return -1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n
        while L <= R:
            mid = L + ((R - L) >> 1)
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                L = mid + 1
            else:
                R = mid - 1
        return L
