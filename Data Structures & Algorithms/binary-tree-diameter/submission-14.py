# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        

        def maxDia(root):
            nonlocal res

            left = self.diameterOfBinaryTree(root.left)
            right = self.diameterOfBinaryTree(root.right)
            res = max(res,left + right)

            return 1 + max(left, right)
        
        maxDia(root)

        return res
