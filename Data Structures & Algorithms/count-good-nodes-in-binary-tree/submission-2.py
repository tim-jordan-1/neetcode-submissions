# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # restrictions
        # n = 10^5

        # while traversing the tree, retain memory of the maximum value from the path

        # check if the current node value is greater than the maximum value found from the path

        # Approach 1: 

        def DFS(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += DFS(node.left, maxVal)
            res += DFS(node.right, maxVal)
            return res
        
        return DFS(root, root.val)

        # Approach 2: nonlocal variable
        res = 0
        def DFS(root, max_val= float('-inf')):
            nonlocal res
            if not root:
                return
            
            if root.val >= max_val:
                print(root.val)
                res += 1
                max_val = root.val
            DFS(root.left, max_val)
            DFS(root.right, max_val)
        DFS(root)
        return res
        