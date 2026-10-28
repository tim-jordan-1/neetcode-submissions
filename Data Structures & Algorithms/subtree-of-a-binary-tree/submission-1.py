# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def sameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            else:
                print("output")
                return False
        
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if node:
                if node.val == subRoot.val:
                    res = sameTree(node, subRoot)
                    if res:
                        return True
                stack.append(node.left)
                stack.append(node.right)
        return res

