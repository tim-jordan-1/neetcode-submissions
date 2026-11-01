# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        # postorder traversal: calculate the max value from the left subtree, then calculate the max value from the right subtree. Finally determine if the values follow the binary search tree rules

        def DFS(node, lower = float("-inf"), upper = float("inf")):
            if not node:
                return True
            if not (lower < node.val and node.val < upper):
                return False
            
            return (DFS(node.left, lower, upper=node.val) and
                   DFS(node.right, lower=node.val, upper=upper))
        
        return DFS(root)

            

            
            
        # postorder traversal
        
        self.isValidBST(root.left)
        self.isValidBST(root.right)
