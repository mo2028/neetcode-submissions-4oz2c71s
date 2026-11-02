# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxSoFar):
            if not node:
                return 0
            res = 0
            if node.val >= maxSoFar:
                res += 1
            maxSoFar = max(maxSoFar, node.val)

            left = helper(node.left, maxSoFar)
            right = helper(node.right, maxSoFar)

            res += left + right 

            return res
        return helper(root, root.val)