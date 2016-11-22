#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '22/11/2016'
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        count = 0

        if nums.count(nums[0]) == len(nums):
            return 1

        for i in xrange(0, len(nums)):
            if nums[i - 1] == nums[i]:
                pass
            else:
                nums[count] = nums[i]
                count += 1
        return count
