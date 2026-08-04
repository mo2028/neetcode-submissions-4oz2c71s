# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

        return False



        


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if both are null then retun true
        if not root and not subRoot:
            return True
        if not root:
            return False
        # # root is null and subroot not null then return false
        # if not root and subRoot:
        #     return False
        # # if there is no subroot is null hten is it a subtree so return truw
        # if root and not subRoot:
        #     return True

        # RECURSIVE CASE
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return False 







        
        