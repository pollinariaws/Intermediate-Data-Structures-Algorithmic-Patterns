from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = deque([(root, root.val)])
        result = []
        while d:
            node, value = d.popleft()
            if node.val >= value:
                result.append((node.val, node.val))
            if node.left:
                d.append((node.left, max(node.left.val, value)))
            if node.right:
                d.append((node.right, max(node.right.val, value)))
        return len(result)
            
                
