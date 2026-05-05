from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def bfs(root):
            d = deque([(root, None)])
            result = []
            while d:
                level = []
                for _ in range(len(d)):
                    node, parent = d.popleft()
                    level.append((node.val, parent))
                    if node.left:
                        d.append((node.left, node))
                    if node.right:
                        d.append((node.right, node))
                result.append(level)
            return result
        level_order = bfs(root)
        for level in level_order:
            vals = {val: parent for val, parent in level}
            if x in vals and y in vals:
                return vals[x] != vals[y]
        return False
