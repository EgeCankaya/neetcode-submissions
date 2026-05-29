# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Walked off the tree without finding a match
        if not root:
            return False
        # Match starts at the current node?
        if self.sameTree(root, subRoot):
            return True
        # Otherwise, keep searching deeper — either side can contain it
        return (self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))

    def sameTree(self, p, q):
        # Both empty: identical (this is the bottom-out case)
        if not p and not q:
            return True
        # Exactly one empty: structural mismatch
        if not p or not q:
            return False
        # Values differ: not identical
        if p.val != q.val:
            return False
        # Values match — both subtrees must also match
        return (self.sameTree(p.left, q.left)
                and self.sameTree(p.right, q.right))