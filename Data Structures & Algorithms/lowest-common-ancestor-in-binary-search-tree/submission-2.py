# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use the current nodes val as a way to direct which is the next branch to go down to

        def checkInBetween(root, p, q):
            if p.val <= root.val and root.val <= q.val: return True
            if q.val <= root.val and root.val <= p.val: return True
            else: return False
        
        if checkInBetween(root, p, q):
            return root
        
        if root.val <= p.val and root.val <= q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)