class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preorder(root, 0, res)
        return res
        
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.val)
            if root.left != None:
                self.preorder(root.left, level+1, res)
            if root.right != None:
                self.preorder(root.right, level+1, res)