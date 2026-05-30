# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        def isBST(node, right, mVal):
            nonlocal res
            
            if not node:
                return
            
            if right:
                if node.val > mVal:
                    mVal = node.val
                else:
                    res = False
            else:
                if node.val < mVal:
                    mVal = node.val
                else:
                    res = False
            isBST(node.left, False, mVal)
            isBST(node.right, True, mVal)

        return res