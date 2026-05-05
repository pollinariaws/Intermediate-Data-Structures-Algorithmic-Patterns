# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        def dfs(root):
            stack = [(root, root.val, [root.val])]
            result = []
            while stack:
                node, s, path = stack.pop()
                if node.left:
                    new_path = path + [node.left.val]
                    stack.append((node.left, s+node.left.val, new_path))
                if node.right:
                    new_path = path + [node.right.val]
                    stack.append((node.right, s+node.right.val, new_path))
                if not node.left and not node.right:
                    if s == targetSum:
                        result.append(path)
            return result
        return (dfs(root))

    
