#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '19/11/2016'
"""


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sll(root, left=False):
            if root == None:
                return 0

            if left and root.left == None and root.right == None:
                return root.val

            return sll(root.left, True) + sll(root.right)

        return sll(root)
