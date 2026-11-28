# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        
        def dfs(root):
            # Add an if statement to short-circuit when we know it's not balanced
            if self.balanced == False or not root:
                return 0
            
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)

            if abs(left_subtree - right_subtree) > 1:
                self.balanced = False
            
            return 1 + max(left_subtree, right_subtree)
        
        dfs(root)
        return self.balanced