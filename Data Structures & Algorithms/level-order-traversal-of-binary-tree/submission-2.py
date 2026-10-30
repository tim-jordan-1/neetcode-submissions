# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #APPROACH: deque

        if not root:
            return []
            
        # type: node, depth
        stack = deque([(root, 0)])
        res = []

        while stack:
            node, depth = stack.popleft()
            if len(res) < depth + 1:
                res.append(list())
            
            res[depth].append(node.val)

            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
            
        return res


        #APPROACH: Recursive function

        res = []
        def DFS(root, depth=0):
            nonlocal res

            if not root:
                return

            if len(res) < depth + 1:
                res.append(list())
            
            res[depth].append(root.val)

            DFS(root.left, depth + 1)
            DFS(root.right, depth + 1)
        
        DFS(root)
        return res