from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        d = deque([root])
        result = []
        while d:
            node = d.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    result.append(node.left.val)
                d.append(node.left)
            if node.right:
                d.append(node.right)
        return sum(el for el in result)
