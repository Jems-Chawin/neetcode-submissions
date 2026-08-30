# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balance = True

        def maxDepth(root):
            if root is None: return 0
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            if abs(left_depth - right_depth) > 1:
                self.is_balance = False
            return max(left_depth, right_depth) + 1

        maxDepth(root)
        return self.is_balance