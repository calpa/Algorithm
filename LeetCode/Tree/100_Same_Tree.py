#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '19/11/2016'
"""


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p == None and q == None:
            return True
        elif p == None or q == None:  # Check this first: 59ms -> 29ms...
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False