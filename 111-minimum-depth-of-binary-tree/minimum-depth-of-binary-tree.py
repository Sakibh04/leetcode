# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        def dfs(node):
            if node is None:
                return 0
                
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            if node.left is None:
                return right_depth + 1

            if node.right is None:
                return left_depth + 1

            return min(left_depth, right_depth) + 1

        return dfs(root)