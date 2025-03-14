# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        bst = None
        while root:
            if root.val == val:
                bst = root
                break
            elif val < root.val:
                root = root.left
            else:
                root = root.right


        return bst

