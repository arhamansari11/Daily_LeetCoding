# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node , maxVal):
            if not node:
                return 0
            count = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal , node.val)
            count += dfs(node.left , maxVal)
            count += dfs(node.right , maxVal)
            return count
        
        return dfs(root , root.val)