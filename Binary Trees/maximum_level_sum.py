from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = deque([root])
        result = []
        while d:
            level = []
            for _ in range(len(d)):
                node = d.popleft()
                level.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            result.append(level)
        sums = [sum(l) for l in result]
        return sums.index(max(sums)) + 1
        
        

