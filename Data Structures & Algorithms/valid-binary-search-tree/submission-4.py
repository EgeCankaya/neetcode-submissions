# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def isBST(node, min_val, max_val):
            nonlocal res
            
            if not node:
                return
            
            if not (min_val < node.val < max_val):
                res = False
                return 

            isBST(node.left, min_val, node.val)
            
            isBST(node.right, node.val, max_val)

        isBST(root, float('-inf'), float('inf'))

        return res