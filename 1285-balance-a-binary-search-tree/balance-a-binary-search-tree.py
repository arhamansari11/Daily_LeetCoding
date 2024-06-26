# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        a = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
        def build(left , right):
            if right < left:
                return None
            mid = left +  right >> 1 
            node = TreeNode(a[mid])
            node.left = build(left , mid-1)
            node.right = build(mid+1 , right)
            return node

        inorder(root)    
        return build(0 , len(a)-1)