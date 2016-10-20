#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '20/10/2016'
"""


def viral_advertising(n):

    total = 5  # Start from 5 people
    answer = 0

    for x in xrange(n):
        like = total / 2
        total = like * 3
        answer += like

    print answer
