# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def DFS(root, depth=0):
            nonlocal res
            if not root:
                return
            if len(res) <= depth:
                res.append(root.val)
            
            DFS(root.right, depth + 1)
            DFS(root.left, depth + 1)
        DFS(root)
        return res
            
        