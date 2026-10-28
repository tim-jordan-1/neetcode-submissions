# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        dq = deque([(p, q)])
        print(dq)
        res = True

        def match(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            elif not node2 and node1:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return True
        while dq:
            node1, node2 = dq.popleft()

            if not match(node1, node2):
                res = False
                break
            
            if node1 and node2:
                dq.append((node1.left, node2.left))
                dq.append((node1.right, node2.right))
        return res
            
                