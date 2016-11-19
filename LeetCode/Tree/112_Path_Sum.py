#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '19/11/2016'
"""


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left == None and root.right == None:
            return root.val == sum

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)