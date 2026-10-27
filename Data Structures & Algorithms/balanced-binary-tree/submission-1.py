# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True
        def calcDepth(root):
            nonlocal res
            if not root:
                return 0
            left_height = calcDepth(root.left)
            right_height = calcDepth(root.right)

            if abs(left_height - right_height) > 1:
                res = False

            return max(left_height, right_height) + 1
        calcDepth(root)
        return res

        