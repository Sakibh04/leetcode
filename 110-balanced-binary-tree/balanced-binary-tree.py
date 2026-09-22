# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.balanced = True

        def dfs(node):
            if node is None:
                return True

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if abs(left_depth - right_depth) > 1:
                self.balanced = False
            
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.balanced