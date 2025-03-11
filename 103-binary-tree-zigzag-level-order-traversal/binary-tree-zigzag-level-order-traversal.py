# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        level = 1
        res = []
        while q:
            level_num = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level_num.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level % 2 == 0:
                level_num.reverse()

            res.append(level_num)
            
            level += 1

        return res