#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '17/11/2016'
"""
import re


def length_of_last_word(s):
    return len(s.strip().split(' ')[-1])


def regex_last_word(s):
    regex = '[a-zA-Z]+'

    if re.search(regex, s):
        return len(re.findall(regex, s)[-1])
