# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        dq = deque([])
        res = True
        def traverseTree(root, check=False):
            nonlocal dq
            nonlocal res
            if not root:
                if not check:
                    dq.append(root)
                else:
                    og_val = dq.popleft()
                    if og_val != root:
                        res = False
                        return
                return
            
            if not check:
                dq.append(root.val)
            else:
                og_val = dq.popleft()
                if og_val != root.val:
                    res = False
                    return
            traverseTree(root.left, check)
            traverseTree(root.right, check)
        traverseTree(p)
        print(dq)
        traverseTree(q, True)
        print(dq)
        return res
            
                