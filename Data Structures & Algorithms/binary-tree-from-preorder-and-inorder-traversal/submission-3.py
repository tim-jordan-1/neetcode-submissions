# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right

        # create hash map to make it easier to find index for root in inorder list
        hashmap = {val:index for index, val in enumerate(inorder)}
        
        # tracker for current root we're looking at
        self.pre_index = 0

        # recursive DFS
        def DFS(l, r):

            # Return None if no nodes are found in bounds
            if l > r:
                return None

            # create root node
            root_val = preorder[self.pre_index]
            root = TreeNode(root_val)

            # find index of root in inorder list -> divides left subtree and right subtree
            mid = hashmap[root_val]

            # incremenent preorder traversal by one
            self.pre_index += 1

            # traverse through left subtree 
            root.left = DFS(l, mid-1)

            # traverse through right subtree
            root.right = DFS(mid+1, r)
            return root

        return DFS(0, len(preorder) - 1)