#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '1/11/2016'
"""


def is_vowel(char):
    # return true if char is a vowel
    return char in 'aeiouAEIOU'


def reverse_vowels(word):
    # Goal: reverse the order of vowels only
    word = list(word)
    left = 0
    right = len(word) - 1
    while left < right:
        if is_vowel(word[left]) and is_vowel(word[right]):
            # swap word[left] and word[right]
            word[left], word[right] = word[right], word[left]
            # select next char
            left += 1
            right -= 1
        elif is_vowel(word[left]):
            # Move the right pointer
            right -= 1
        else:
            # Move the left pointer
            left += 1

    return ''.join(word)

