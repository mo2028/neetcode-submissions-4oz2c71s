# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BASE CASE
        # both null at the same time return true
        if not p and not q:
            return True
        # just one null, then return false
        if not p or not q:
            return False
        if not q or not p:
            return False


        # RECURSIVE CASE
        # recurse on both the trees and if either one comes back false then that means that the whole solution is false so return
        if p.val == q.val:
            # self.isSameTree(p.left, q.left)
            # self.isSameTree(p.right, q.right)
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
            



        
        
        