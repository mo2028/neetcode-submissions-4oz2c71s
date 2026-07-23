# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # thinking  about base cases first
        # root is none, then 0
        # root does not have any children, then 1
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return 1

        # at any level 
        # return 1 + max(maxDepth(node.left), maxDepth(node.right))) 
        # dfs
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))





        