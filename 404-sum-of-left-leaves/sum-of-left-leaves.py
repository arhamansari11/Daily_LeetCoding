# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        sum_leaf = 0

        # Check if the left child is a left leaf
        if root.left and not root.left.left and not root.left.right:
            sum_leaf += root.left.val  # Add value if it's a left leaf
        else:
            sum_leaf += self.sumOfLeftLeaves(root.left)  # Recur for left child

        # Always recur for right child, regardless of its type
        sum_leaf += self.sumOfLeftLeaves(root.right)

        return sum_leaf
