# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def dfs(root):
            stack = [(root, root.val)]
            while stack:
                node, s = stack.pop()
                if node.left:
                    stack.append((node.left, s+node.left.val))
                if node.right:
                    stack.append((node.right, s+node.right.val))
                if not node.left and not node.right:
                    if s == targetSum:
                        return True
            return False
        return dfs(root)

                
