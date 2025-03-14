# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        count = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    count += 1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)


        return count
