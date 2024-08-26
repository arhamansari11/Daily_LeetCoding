# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         # Each node in an n-ary tree has a value and a list of children
#         # If no children are provided, default to an empty list
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []  # This list will store the result of the postorder traversal
        
        # Recursive function to perform postorder traversal
        def postorder(node):
            if not node:  # Base case: if node is None, return
                return
            
            # Iterate over each child of the current node
            for child in node.children:
                postorder(child)  # Recursively call postorder on the child node
                
            arr.append(node.val)  # After processing all children, append the current node's value
        
        postorder(root)  # Start the traversal from the root node
        return arr  # Return the final list containing the postorder traversal result
