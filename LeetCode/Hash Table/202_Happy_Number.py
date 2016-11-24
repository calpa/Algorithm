#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '24/11/2016'
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number = {}
        while True:
            number[n] = 1
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n /= 10
            n = temp
            if n == 1 or n in number:
                break
        return n == 1
