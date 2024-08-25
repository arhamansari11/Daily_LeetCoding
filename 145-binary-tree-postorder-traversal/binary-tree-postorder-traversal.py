# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def postorder(node):
            if not node:
                return None
            postorder(node.left)
            postorder(node.right)
            arr.append(node.val)
        postorder(root)
        return arr
        