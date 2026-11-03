# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        k_val = 0
        def DFS(node):
            nonlocal res
            nonlocal k_val
            if not node:
                return 0
            
            k_val = DFS(node.left) + k_val + 1
            if k_val == k:
                res = node.val
            
            return DFS(node.right)
        DFS(root)
        return res