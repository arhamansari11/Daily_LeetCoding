# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        arr = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            maximum = float('-inf')
            for i in range(qLen):
                node = q.popleft()
                if node:
                    maximum = max(maximum , node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            
            arr.append(maximum)

        return arr


        

