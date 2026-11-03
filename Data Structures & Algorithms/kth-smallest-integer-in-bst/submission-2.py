# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # APPROACH: Iterative DFS (Optimal)
        n = 0
        stack = []
        curr = root

        while stack and curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            n += 1
            curr = stack.pop()
            if n == k:
                return curr.val
            curr.right

        # APPROACH: recursive in-order traversal
        # Time complexity: O(n)
        # Space complexity: O(h) for recursion stack, worst-case O(n)
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