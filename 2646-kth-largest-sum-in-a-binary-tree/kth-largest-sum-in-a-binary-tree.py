# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        q = deque()
        q.append(root)
        while q:
            addition = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    addition += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            array.append(addition)
        array.sort(reverse=True)

        if k > len(array) or k <= 0:
            return -1  
        return array[k-1]