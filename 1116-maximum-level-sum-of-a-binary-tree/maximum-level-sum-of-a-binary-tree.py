# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        level = 1
        level_track = 1
        max_val = root.val
        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level_sum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level_sum > max_val:
                max_val = level_sum
                level = level_track

            level_track += 1

        return level