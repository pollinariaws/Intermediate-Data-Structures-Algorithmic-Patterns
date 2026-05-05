# Definition for a binary tree node.
# class TreeNode:
from collections import deque
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = deque([root])
        result = []
        while d:
            node = d.popleft()
            if node is not None:
                result.append(node.val)
                node.left, node.right = node.right, node.left
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return root
