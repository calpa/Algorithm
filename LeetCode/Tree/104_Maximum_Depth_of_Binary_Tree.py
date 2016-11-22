#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'calpa'
__mtime__ = '22/11/2016'
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def md(root, level=1):
            if root:
                # Check if root
                if root.left == None and root.right == None:
                    return level

                l, r = 0, 0

                if root.left:
                    l = md(root.left, level + 1)
                if root.right:
                    r = md(root.right, level + 1)
                # max(l,r)
                if l > r:
                    return l
                else:
                    return r
            else:
                return 0

        return md(root)
