# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        add = 0
        def helper(node):
            nonlocal add
            if node == None:
                return 
            helper(node.right)
            add += node.val
            node.val = add
            helper(node.left)
        helper(root)

        return root
            