"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # recursion approach
        stack = []
        
        if root == None:
            return stack
        
        def recursion(root, stack):
            for child in root.children:
                recursion(child, stack)
            stack.append(root.val)
        recursion(root, stack)
        
        return stack
    
    
#Time complexity: O(N)
#Space complexity: O(N)