# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertNode(node):
            if not node:
                node = TreeNode(val)
            elif val < node.val:
                node.left = insertNode(node.left)
            else:
                node.right = insertNode(node.right)

            return node


        return insertNode(root)