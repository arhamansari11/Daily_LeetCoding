# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(node , currSum):
            if not node:
                return False
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            return (path(node.left , currSum)) or (path(node.right , currSum))
        
        return path(root , 0)