# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def maxDepth(root):
            if root is None: return 0

            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            self.max_diameter = max(left_depth + right_depth, self.max_diameter)

            return max(left_depth, right_depth) + 1
        
        maxDepth(root)
        return self.max_diameter
