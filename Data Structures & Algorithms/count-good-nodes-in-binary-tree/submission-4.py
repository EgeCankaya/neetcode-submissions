# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 1
        res = 1

        def isGood(node, mVal):
            nonlocal res
            
            if not node:
                return
            
            if node.val >= mVal:
                res += 1
                mVal = node.val

            isGood(node.left, mVal)
            isGood(node.right, mVal)

        isGood(root, root.val)

        return res


        