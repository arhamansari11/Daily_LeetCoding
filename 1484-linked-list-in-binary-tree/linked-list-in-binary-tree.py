class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head , node):
            if not head:
                return True
            if not node:
                return False
            if head.val == node.val:
                return dfs(head.next , node.left) or dfs(head.next, node.right)
            return False
        if not root:
            return False
        return dfs(head , root) or self.isSubPath(head , root.left) or self.isSubPath(head , root.right)